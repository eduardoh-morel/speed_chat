import socket
import threading

HOST = '0.0.0.0'  
PORT = 5000  

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

def receber_mensagens():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            print(mensagem)
        except:
            print("Erro ao receber mensagem.")
            cliente.close()
            break

def enviar_mensagens():
    while True:
        mensagem = input('')
        cliente.send(mensagem.encode('utf-8'))

# Inicializa as threads para envio e recebimento de mensagens
thread_receber = threading.Thread(target=receber_mensagens)
thread_receber.start()

thread_enviar = threading.Thread(target=enviar_mensagens)
thread_enviar.start()
