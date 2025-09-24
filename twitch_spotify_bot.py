import irc.bot
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# ---------- CONFIGURAÇÕES ----------
TWITCH_CHANNEL = "#TWITCH_CHANNEL" # Seu @ da Twitch
TWITCH_NICK = "#TWITCH_NICK" # Seu Nick da Twitch
TWITCH_TOKEN = "oauth:TWITCH_TOKEN" # Seu Token da Twitch

MODS = ["Mod1", "Mod2", "Mod3"]

SPOTIFY_CLIENT_ID = "SPOTIFY_CLIENT_ID" # Seu ID de Cliente do Spotify
SPOTIFY_CLIENT_SECRET = "SPOTIFY_CLIENT_SECRET" # Seu Secredo de Cliente do Spotify
SPOTIFY_REFRESH_TOKEN = "SPOTIFY_REFRESH_TOKEN"  # Seu Token de Restauração

SCOPE = "user-modify-playback-state user-read-playback-state"
REDIRECT_URI = "https://localhost:8888/callback"
# -----------------------------------

# Função para criar cliente Spotify usando refresh token
def create_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        open_browser=False
    )
    # Gera access token a partir do refresh token
    token_info = auth_manager.refresh_access_token(SPOTIFY_REFRESH_TOKEN)
    return spotipy.Spotify(auth=token_info['access_token'])

sp = create_spotify_client()

print("Iniciando Bot...")

class SongRequestBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        irc.bot.SingleServerIRCBot.__init__(self,
            [("irc.chat.twitch.tv", 6667, TWITCH_TOKEN)],
            TWITCH_NICK, TWITCH_NICK)
    
    def on_welcome(self, c, e):
        print(f"Entrando no canal {TWITCH_CHANNEL}...")
        c.join(TWITCH_CHANNEL)

    def on_pubmsg(self, c, e):
        msg = e.arguments[0]
        print(f"[CHAT] {e.source.nick}: {msg}")
        if msg.startswith("!sr "):
            song = msg[4:]
            try:
                results = sp.search(q=song, type="track", limit=1)
                if results["tracks"]["items"]:
                    track = results["tracks"]["items"][0]
                    sp.add_to_queue(track["uri"])
                    c.privmsg(TWITCH_CHANNEL, f"🎵 {track['name']} de {track['artists'][0]['name']} foi adicionada à fila!")
                else:
                    c.privmsg(TWITCH_CHANNEL, f"❌ Música não encontrada: {song}")
            except Exception as err:
                print("Erro Spotify:", err)
                c.privmsg(TWITCH_CHANNEL, "❌ Erro ao adicionar música.")

        if msg.startswith("!clear"):
            user = e.source.nick
            if user.lower() in [m.lower() for m in MODS]:
                try: 
                    playback = sp.current_playback()
                    if playback is None:
                        c.privmsg(TWITCH_CHANNEL, "Nenhuma reprodução ativa no momento.")
                    else:
                        for _ in range(300): 
                            playback = sp.current_playback()
                            if playback is None or playback['item'] is None:
                                break
                            sp.next_track()
                            time.sleep(0.05)
                        c.privmsg(TWITCH_CHANNEL, "Fila de reprodução limpada!")
                except Exception as err:
                    print("Erro ao limpar a fila:", err)
                    c.privmsg(TWITCH_CHANNEL, "Erro ao limpar a fila!")
            else:
                c.privmsg(TWITCH_CHANNEL, "Apenas moderadores autorizados podem usar este comando!")

        if msg.startswith("!skip"):
            user = e.source.nick
            if user.lower() in [m.lower() for m in MODS]:
                try: 
                    playback = sp.current_playback()
                    if playback is None:
                        c.privmsg(TWITCH_CHANNEL, "Nenhuma música está sendo tocada.")
                    else:
                        sp.next_track()
                except Exception as err:
                    print("Erro ao pular a música:", err)
                    c.privmsg(TWITCH_CHANNEL, "Erro ao pular a música!")
            else:
                c.privmsg(TWITCH_CHANNEL, "Apenas moderadores autorizados podem usar este comando!")
# Inicia o bot
SongRequestBot().start()
