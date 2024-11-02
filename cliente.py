import socket
import threading

# Configurações do cliente
HOST = '10.1.24.10'  # Deve ser o mesmo IP do servidor
PORT = 5000  # Mesma porta do servidor

# Inicializa o socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Função para receber mensagens do servidor
def receber_mensagens():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            print(mensagem)
        except:
            print("Erro ao receber mensagem.")
            cliente.close()
            break

# Função para enviar mensagens para o servidor
def enviar_mensagens():
    while True:
        mensagem = input('')
        cliente.send(mensagem.encode('utf-8'))

# Inicializa as threads para envio e recebimento de mensagens
thread_receber = threading.Thread(target=receber_mensagens)
thread_receber.start()

thread_enviar = threading.Thread(target=enviar_mensagens)
thread_enviar.start()