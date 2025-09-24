# Como Usar este Bot

## Passo 1: Criar aplicativo no Spotify
Vá para https://developer.spotify.com/dashboard e logue com sua conta Spotify, e então, crie um novo aplicativo. Coloque um nome e descrição, e coloque essa URL de redirecionamento: https://spotify-refresh-token-generator.netlify.app
Salve o ID de Cliente e o Secredo de Cliente em um local seguro.

<img width="649" height="469" alt="image" src="https://github.com/user-attachments/assets/724e6c98-1277-44de-bcfb-56b794a09b4c" />
<img width="941" height="399" alt="image" src="https://github.com/user-attachments/assets/e4cb5a5f-8b33-4829-9c74-e46804780a8c" />




## Passo 2: Pegar seu Token da Twitch
Acesse https://twitchtokengenerator.com/ e logue sua conta, e guarde seu token no mesmo lugar em que guardou os tokens do Spotify

<img width="606" height="320" alt="image" src="https://github.com/user-attachments/assets/99385a4f-d217-42f7-a35c-8bf6397b97ec" />
<img width="853" height="161" alt="image" src="https://github.com/user-attachments/assets/d7f663ab-3d61-4660-9037-b35ea44ffb20" />



## Passo 3: Baixar e rodar o bot!
Acesse https://spotify-refresh-token-generator.netlify.app e insira os tokens que você salvou antes, ele irá te dar um Token de Restauração. Agora com todas essas informações, baixe o arquivo python do bot, e abra ele em um editor (de preferência VS Code)

Substitua TWITCH_CHANNEL pelo seu @ da Twitch, seguindo o formato: "#seu_@_aqui"
Substitua TWITCH_NICK pelo seu nick na twitch, seguindo o formato: "#Seu_Nick_Aqui"
Substitua TWITCH_TOKEN pelo token gerado no passo 2, seguindo o formato: "oauth:SEU_TOKEN_AQUI"

Substitua SPOTIFY_CLIENT_ID pelo seu Token de Cliente gerado no passo 1
Substitua SPOTIFY_CLIENT_SECRET pelo seu Secredo de Cliente, gerado no passo 1
Substitua SPOTIFY_REFRESH_TOKEN pelo Token de Restauração gerado no passo 1, pelo site https://spotify-refresh-token-generator.netlify.app

Substitua MOD1, MOD2, MOD3 e etc pelos seus moderadores e por você mesmo!

<img width="734" height="254" alt="image" src="https://github.com/user-attachments/assets/70d07613-3f3d-41c7-8f2d-6cbe8743dcda" />

Rode este programa usando o comando "Python CAMINHO/DO/PROGRAMA.py", você pode adicioná-lo para iniciar automaticamente em segundo plano se quiser.
### Aviso: O bot só irá funcionar enquanto o Spotify estiver aberto e tocando alguma música!
