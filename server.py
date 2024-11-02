import socket
import threading

# Configurações do servidor
HOST = '10.1.24.10'  # Endereço IP local (para testes locais)
PORT = 5000  # Porta de comunicação

# Inicializa o socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clientes = []  # Lista para armazenar todos os clientes conectados

# Função para enviar mensagem para todos os clientes conectados
def broadcast(mensagem, cliente):
    for cl in clientes:
        if cl != cliente:
            try:
                cl.send(mensagem)
            except:
                cl.close()
                clientes.remove(cl)

# Função para lidar com a conexão de cada cliente
def handle_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            broadcast(mensagem, cliente)
        except:
            clientes.remove(cliente)
            cliente.close()
            break

# Função principal do servidor
def main():
    print("Servidor rodando...")
    while True:
        cliente, endereco = server.accept()
        print(f"Conexão estabelecida com {endereco}")
        clientes.append(cliente)
        thread = threading.Thread(target=handle_cliente, args=(cliente,))
        thread.start()

main()