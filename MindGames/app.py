from flask import Flask, render_template
from flask_sock import Sock

# Initialize Flask application and WebSocket extension
app = Flask(__name__)
sock = Sock(app)

# Default route, displays Pac-Man
@app.route('/')
def index():
    # Render the index template
    return render_template('index.html')

# WebSocket route for sending and receiving data to the displayed page
@sock.route('/obci')
def obci(sock):
    while True:
        data = sock.receive()
        sock.send(data)

# If this module is being run directly, run the Flask application
if __name__ == '__main__':
    app.run(debug=True)