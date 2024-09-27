# TwitchChatBot 🤖

**TwitchChatBot** é um chatbot interativo para Twitch, projetado para simular conversas entre múltiplos bots e interagir com espectadores em tempo real. Ele alterna automaticamente entre vários temas e utiliza a API do Llama para gerar respostas realistas, criando uma experiência de chat dinâmica e envolvente.

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

Para conectar seu bot à Twitch, você precisa gerar um token de autenticação. Siga os passos abaixo para configurar a Twitch com o **hackersBashTwitchBot**:

#### 2.1. Gerar Token de Autenticação

1. Acesse [TwitchApps TMI](https://twitchapps.com/tmi/) e gere seu token OAuth.
2. Esse token será usado no arquivo de configuração para conectar o bot à Twitch.

#### 2.2. Clonar o Projeto do Bot IRC

Clone o projeto **hackersBashTwitchBot** para configurar a conexão IRC com a Twitch:
```bash
git clone https://github.com/tixlegeek/hackersBashTwitchBot.git
```

#### 2.3. Configurar o Bot

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
---

### Contribuições

Contribuições são bem-vindas! Se você deseja adicionar novos recursos ou otimizar o chatbot, sinta-se à vontade para abrir um *pull request*.

---

### Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
