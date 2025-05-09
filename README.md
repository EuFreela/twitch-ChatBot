# Twitch-Chat-Bot 🤖

**TwitchChatBot** é um chatbot interativo para Twitch, projetado para simular conversas entre múltiplos bots e interagir com espectadores em tempo real. Ele alterna automaticamente entre vários temas e utiliza a API do Llama para gerar respostas realistas, criando uma experiência de chat dinâmica e envolvente.

A utilização de IA em bots de chat pode ser uma ótima ferramenta para manter a conversa fluindo em canais menores da Twitch. No entanto, é importante ajustar seu prompt para garantir que esteja em conformidade com as políticas da plataforma. Além disso, você pode integrar um chatbot como o [Nightbot](https://nightbot.tv/) para ajudar na moderação e gerenciamento do chat, garantindo um ambiente mais controlado. Embora os bots ajudem a criar movimento no canal, eles não substituem a interação com pessoas reais. 

Este projeto foi desenvolvido como uma alternativa às APIs pagas e com limitações, como o [ChatGPT](https://platform.openai.com/docs/api-reference) e o [Cohere](https://cohere.com/). Usando o LLaMA localmente, você terá um chatbot rodando em seu próprio computador, sem restrições de uso ou limites de chamadas, pelo menos por enquanto.

### Principais Funcionalidades:

- **Chat Automatizado**: Simula interações realistas entre bots no chat da Twitch.
- **Temas Dinâmicos**: Alterna entre temas como jogos, tecnologia, cultura pop, emojis, etc.
- **Respostas Direcionadas**: Responde diretamente a menções de usuários no chat da Twitch.
- **Interações com Emojis**: Tema especial dedicado a interações com emojis, variando entre 1 e 4 emojis por mensagem.
- **Integração com LLM (Llama)**: Utiliza o **Ollama Llama** para gerar respostas dinâmicas e realistas.

### Tecnologias Utilizadas:

- **Python**: Backend principal para gerenciar as interações.
- **Ollama Llama**: Modelo de linguagem para gerar respostas dinâmicas.
- **Socket e IRC**: Conexão com o chat da Twitch via IRC.
- **API do Ollama**: Para gerar respostas dinâmicas via Llama.
- **Troca de Temas**: Alternância automática de temas a cada intervalo configurado.

---

## Instalação

### 1. Instalação do Llama

Primeiro, você precisa instalar o **Ollama Llama** para executar o modelo localmente. Siga as etapas abaixo para configurar:

#### 1.1. Instalar o Ollama

Baixe e instale o Ollama seguindo as instruções do site oficial:

- [Instruções para Instalação do Ollama](https://ollama.com/download)

#### 1.2. Documentação da API do Llama

Para utilizar a API local do Llama, consulte a documentação oficial:

- [Documentação da API do Ollama](https://github.com/ollama/ollama/blob/main/docs/api.md)

#### 1.3. Configuração da API do Llama no Código

O chatbot faz requisições à API local do Llama. As requisições são feitas através do endpoint `http://localhost:11434/api/generate`. Certifique-se de que o Llama está rodando localmente para que as chamadas da API funcionem corretamente.

### 2. Configuração da Twitch (IRC)

Para conectar seu bot à Twitch, você precisa gerar um token de autenticação. Siga os passos abaixo para configurar a Twitch:

#### 2.1. Gerar Token de Autenticação

1. Acesse [TwitchApps TMI](https://twitchapps.com/tmi/) e gere seu token OAuth.
2. Esse token será usado no arquivo de configuração para conectar o bot à Twitch.
3. Se preferir desinstalar entre no seu canal em [configuracoes, clique aqui](https://www.twitch.tv/settings/connections), role o mouse e busque por **Twitch Chat OAuth Token Generator**. Clique no botão **desligar**

#### 2.2. Configurar o Bot

Edite o arquivo de configuração do bot com o token gerado e os detalhes do canal da Twitch. No seu arquivo Python, configure a conexão usando o token e o nome de usuário da Twitch:

```python
NICK = "seu_nome_de_usuario_twitch"
PASS = "oauth:seu_token"
CHANNEL = "#nome_do_canal"
```

---

### Como Usar

1. **Clonar este repositório** e seguir as instruções acima para configurar o Llama e o IRC da Twitch.
2. **Iniciar o bot**: Execute o script para ver as interações dinâmicas no seu canal da Twitch.
   ```bash
   pip install -r requirements.txt
   python twitchChatBot.py
   ```
3. **Customização de Temas**: Personalize os temas e emojis no código para adequar o chatbot ao seu canal.
4. **Twitch**: entre no seu canal, Gestor de Transmissões. Inicie o chat com alguma frase. O chat será iniciado.
5. **Barrar o chat**: abra o powershell e digite: **Stop-Process -Name python -Force**

---

### Contribuições

Contribuições são bem-vindas! Se você deseja adicionar novos recursos ou otimizar o chatbot, sinta-se à vontade para abrir um *pull request*.

---

### Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
