import socket
import threading

HOST = '0.0.0.0' 
PORT = 5000 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clientes = []  

def broadcast(mensagem, cliente):
    for cl in clientes:
        if cl != cliente:
            try:
                cl.send(mensagem)
            except:
                cl.close()
                clientes.remove(cl)

def handle_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            broadcast(mensagem, cliente)
        except:
            clientes.remove(cliente)
            cliente.close()
            break

def main():
    print("Servidor rodando...")
    while True:
        cliente, endereco = server.accept()
        print(f"Conexão estabelecida com {endereco}")
        clientes.append(cliente)
        thread = threading.Thread(target=handle_cliente, args=(cliente,))
        thread.start()

main()
