from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

@sock.route('/obci')
def obci(sock):
    while True:
        data = sock.receive()
        sock.send(data)

if __name__ == '__main__':
    app.run(debug=True)