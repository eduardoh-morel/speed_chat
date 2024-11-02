from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

historico_mensagens = []

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('connect')
def handle_connect():
    
    emit('historico', historico_mensagens)

@socketio.on('message')
def handle_message(data):
    
    hora = datetime.now().strftime('%H:%M')
    data['hora'] = hora
    
    historico_mensagens.append(data)
    
    if len(historico_mensagens) > 100:
        historico_mensagens.pop(0)
    
    print(f"{data['username']} ({data['hora']}): {data['message']}")
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='10.1.24.10', port=5000)
