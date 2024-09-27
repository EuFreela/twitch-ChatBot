import socket
import threading
import time
import random
import os
import requests

# Variáveis para configurar o intervalo de tempo de resposta
tempo_resposta_min = 5  # Tempo mínimo (em segundos)
tempo_resposta_max = 50  # Tempo máximo (em segundos)

# Configuração dos temas com seus tempos em segundos
jogo = "nome_do_game_da_gameplay"
temas = [
    {"tema": f"{jogo} é o jogo de hoje na gameplay", "tempo": 20},
    {"tema": f"tecnologia do game {jogo}", "tempo": 20},
    {"tema": f"música do game {jogo}", "tempo": 20},
    {"tema": f"cinemática do game {jogo}", "tempo": 20},
    {"tema": f"emojs", "tempo": 5}  # Tema especial para emojis
]

# Lista de mensagens de erro aleatórias
mensagens_erro = [
    "Opa, nossa 🤖💥, hahaha não entendi foi nada!",
    "Eita, deu ruim aqui 😅! to viajando!",
    "Acho que o robô dormiu 💤, tenta de novo mais tarde!",
    "Ops, 🤷‍♂️! Me dá um minutinho!",
    "Tá difícil! 😵 cararro!",
    "Não foi dessa vez 😬, mas daqui a pouco funciona!",
    "Bugou geral! 🤖 Vou tentar de novo mais tarde.",
    "Opa! Algo deu errado aqui, mas a gente tenta de novo 😂.",
    "Hmm... parece que algo se perdeu no caminho 😅. que mierdas!"
]

# Palavras a serem removidas nas respostas
palavras_proibidas = ["Eu sou uma IA criativa", "IA", "AI", "Bot", "bot", "anfitriã bot", "sou bot"]

# Lista de usuários e tokens
usuarios = [
    {"nome": "usuario_canal_twitch", "token": "oauth:xxxxxxxxxxxxxxxxxxxxxxx"}
]

# Canal onde todos estão conectados
channel = '#meu_canal_twitch'  

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Função para gerar texto usando a API do Ollama
def gerar_texto(texto):
    url = 'http://localhost:11434/api/generate'  # Endpoint da API do Ollama

    # Dados do payload para enviar à API
    prompt = f"Responda de forma concisa e com no máximo 120 caracteres. {texto}"
    payload = {
        'model': 'llama3.2',
        'prompt': prompt,
        'stream': False,
        'temperature': 0.7,  # Mais conservador e focado
        'max_tokens': 40 
    }

    try:
        # Fazendo a requisição POST à API do Ollama
        response = requests.post(url, json=payload)

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            data = response.json()
            return data.get('response', 'Nenhuma resposta encontrada.')
        else:
            return f"Erro na API: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Erro ao se comunicar com a API: {e}"

# Variável para controlar o tempo para mudar de tema
ultimo_tema_trocado = time.time()
tempo_atual_tema = None
tempo_tema_restante = 0

# Lista de emojis
import random

emojis = [
    # Emojis de rostos e emoções
    random.choice(["😀", "😃😄", "😁😆", "😂🤣😅", "😊😇"]),
    random.choice(["🙂", "🙃😉", "😍", "🥰", "😋"]),
    random.choice(["😜", "🤪", "😎", "🤩"]),
    random.choice(["😡", "😠", "😤", "😭"]),
    random.choice(["😢", "🤔", "🤨", "😐", "😶"]),
    random.choice(["😏", "🥳", "😎🤓", "🤠", "🧐"]),
    random.choice(["😇", "🥺", "😈", "👿", "👹"]),

    # Emojis de comidas e bebidas
    random.choice(["🍕", "🍔🍟", "🍣", "🍜", "🍩"]),
    random.choice(["🍪🍫", "🍰", "🎂", "🍉🍓"]),
    random.choice(["🍌", "🍍", "🥭", "🍎"]),
    random.choice(["🍏", "🍊🍋", "🍇", "🍕🍟"]),
    random.choice(["🍹", "🍸", "🍷", "🍺"]),

    # Emojis de esportes e jogos
    random.choice(["⚽", "🏀🏈", "⚾", "🎾"]),
    random.choice(["🏓", "🏸🥅", "🏒🏑"]),
    random.choice(["🎮", "🕹️", "👾", "🕹️"]),
    random.choice(["🎲", "🥇", "🥈", "🥉🏆"]),

    # Emojis de natureza e animais
    random.choice(["🌲", "🌳", "🌴🌵"]),
    random.choice(["🌿", "🌸", "🌼"]),
    random.choice(["🌻", "🌹", "🌺"]),
    random.choice(["🐶", "🐱", "🐭🐹"]),
    random.choice(["🐰", "🐻", "🐼🐨"]),
    random.choice(["🐯", "🦁", "🐔🐧"]),
    random.choice(["🐦", "🐤", "🐣🐙"]),
    random.choice(["🦀", "🦞", "🦐🐡"]),

    # Emojis de transportes e viagens
    random.choice(["✈️", "🌍", "🗺️"]),
    random.choice(["🚗", "🚕", "🚂🚊"]),
    random.choice(["🚀", "🛳️", "🚁"]),
    random.choice(["🚴‍♂️", "🚴‍♀️", "🏍️"]),
    random.choice(["🚘", "🛵", "🏙️"]),
    random.choice(["🌆", "🌇", "🏖️"]),
    random.choice(["🏝️", "🧳", "🚪"]),

    # Emojis de tecnologia e dispositivos
    random.choice(["🤖", "💻", "📱"]),
    random.choice(["🖥️", "⌨️", "🖱️"]),
    random.choice(["🖲️", "💽", "💾"]),
    random.choice(["💿", "📡", "📷"]),
    random.choice(["📹", "🎥", "📺"]),

    # Emojis de música e entretenimento
    random.choice(["🎧", "🎤", "🎼"]),
    random.choice(["🎹", "🎸", "🎺"]),
    random.choice(["🎷", "🥁", "🎻"]),
    random.choice(["🎶", "🎬", "📽️"]),
    random.choice(["🎥", "📺", "🎭"]),
    random.choice(["🎮", "🕹️", "🎲"]),
    random.choice(["🎯", "🏹"]),

    # Emojis de objetos e atividades
    random.choice(["💼", "📚", "📖"]),
    random.choice(["📝", "✏️", "🔨"]),
    random.choice(["🔧", "🔩", "⚙️"]),
    random.choice(["🔗", "🔑", "🔒"]),
    random.choice(["🧳", "🛏️", "🚪"]),

    # Emojis de celebração e feriados
    random.choice(["🎉", "🎊", "🎁"]),
    random.choice(["🎀", "🎄", "🎃"]),
    random.choice(["👻", "🎅", "🎇"]),
    random.choice(["🎆", "🧨", "🎈"]),
    random.choice(["🥳", "🎈", "🍾"])
]


# Função para escolher o tema atual baseado no tempo definido
def escolher_tema_atual():
    global ultimo_tema_trocado, tempo_atual_tema, tempo_tema_restante
    tempo_atual = time.time()
    
    # Se o tempo do tema atual acabou, escolhe um novo tema
    if tempo_atual - ultimo_tema_trocado > tempo_tema_restante:
        tema_escolhido = random.choice(temas)
        tempo_atual_tema = tema_escolhido["tema"]
        tempo_tema_restante = tema_escolhido["tempo"]
        ultimo_tema_trocado = tempo_atual
        print(f"Novo tema: {tempo_atual_tema} (por {tempo_tema_restante} segundos)")
    return tempo_atual_tema

# Função para verificar se há uma menção direta a outro usuário
def verificar_mencao_usuario(mensagem):
    if "@" in mensagem:
        partes = mensagem.split(" ")
        for parte in partes:
            if parte.startswith("@"):
                return parte[1:].lower()  # Remove o @ e retorna o nome do usuário mencionado
    return None

# Função para remover menções ao próprio nome do bot
def remover_mencao_proprio_nome(resposta, nome_bot):
    if nome_bot.lower() in resposta.lower():
        resposta = resposta.replace(nome_bot, "").strip()
    return resposta

# Função para gerar resposta com a API do Ollama
def responder_ollama(mensagem_usuario, nome_usuario, remetente):
    try:
        # Escolher o tema atual
        tema_atual = escolher_tema_atual()

        # Se o tema atual for "emojis", retorna uma sequência de emojis
        if tema_atual == "emojs":
            resposta = random.choice(emojis)
            return resposta

        # Verificar se há uma menção direta a outro usuário
        mencionado = verificar_mencao_usuario(mensagem_usuario)
        
        if mencionado:
            # Se o nome mencionado for o do bot, ele deve responder em primeira pessoa
            if mencionado == nome_usuario.lower():
                contexto = (
                    f"Você, '{nome_usuario}', está respondendo diretamente à pergunta de '@{remetente}'. "
                    "Responda diretamente em primeira pessoa, de forma educada e amigável."
                )
            else:
                return None  # Esse bot não deve responder, pois a mensagem não é para ele
        else:
            # Resposta aberta (sem @)
            contexto = (
                f"O assunto do chat é '{tema_atual}'. "
                "Responda de forma divertida e informal, com emojis, e interaja com os outros bots."
            )

        prompt_com_contexto = f"{contexto} O usuário disse: {mensagem_usuario}"
        resposta = gerar_texto(prompt_com_contexto)
        
        # Verificar se a resposta contém palavras proibidas e removê-las
        for palavra in palavras_proibidas:
            if palavra.lower() in resposta.lower():
                resposta = resposta.replace(palavra, '').strip()

        # Remover menção ao próprio nome do bot
        resposta = remover_mencao_proprio_nome(resposta, nome_usuario)

        # Adicionar o @ no início com o remetente, se o bot estiver respondendo diretamente
        if mencionado == nome_usuario.lower():
            resposta = f"@{remetente} {resposta}"

        return resposta
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return random.choice(mensagens_erro)

# Função para enviar mensagem ao chat da Twitch
def enviar_mensagem(sock, channel, mensagem):
    sock.send(f"PRIVMSG {channel} :{mensagem}\n".encode('utf-8'))

# Função para conectar ao IRC da Twitch
def conectar_irc(usuario, token, channel):
    server = 'irc.chat.twitch.tv'
    port = 6667
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {usuario}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    return sock

# Função para gerenciar a conexão de um usuário
def bot_conversa(usuario, token, channel):
    sock = conectar_irc(usuario, token, channel)
    while True:
        response = sock.recv(2048).decode('utf-8')

        # Responde a PINGs do servidor para manter a conexão
        if response.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        
        # Quando uma mensagem for recebida
        elif "PRIVMSG" in response:
            partes = response.split(":", 2)
            remetente = partes[1].split("!")[0]
            mensagem = partes[2].strip()

            print(f"{remetente} ({usuario}): {mensagem}")

            # Verificar se a mensagem contém uma menção (@)
            mencionado = verificar_mencao_usuario(mensagem)

            # Se houver uma menção, responder apenas para o destinatário correto
            if mencionado:
                if mencionado == usuario.lower():
                    resposta_bot = responder_ollama(mensagem, usuario, remetente)
                    if resposta_bot:
                        enviar_mensagem(sock, channel, resposta_bot)
                        print(f"Bot ({usuario}): {resposta_bot}")
                else:
                    print(f"Mensagem mencionada para {mencionado}, ignorando {usuario}.")
                    continue

            # Se não houver menção, os bots interagem entre si
            else:
                if random.choice([True, False]):
                    delay = random.randint(tempo_resposta_min, tempo_resposta_max)
                    time.sleep(delay)  # Adicionar delay para evitar respostas simultâneas
                    resposta_bot = responder_ollama(mensagem, usuario, remetente)
                    if resposta_bot:
                        enviar_mensagem(sock, channel, resposta_bot)
                        print(f"Bot ({usuario}): {resposta_bot}")



# Função principal para iniciar bots simultâneos
def iniciar_bots():
    threads = []
    for usuario in usuarios:
        thread = threading.Thread(target=bot_conversa, args=(usuario["nome"], usuario["token"], channel))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

# Iniciar os bots
iniciar_bots()
