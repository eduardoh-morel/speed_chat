from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Lista para armazenar o histórico de mensagens
historico_mensagens = []

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('connect')
def handle_connect():
    # Envia o histórico de mensagens ao conectar
    emit('historico', historico_mensagens)

@socketio.on('message')
def handle_message(data):
    # Adiciona o horário da mensagem
    hora = datetime.now().strftime('%H:%M')
    data['hora'] = hora
    
    # Armazena a mensagem no histórico
    historico_mensagens.append(data)
    if len(historico_mensagens) > 100:  # Limita o histórico a 100 mensagens
        historico_mensagens.pop(0)
    
    print(f"{data['username']} ({data['hora']}): {data['message']}")
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
