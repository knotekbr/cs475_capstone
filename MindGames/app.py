from flask import Flask, render_template
from flask_sock import Sock
from pylsl import StreamInlet, resolve_stream

# Initialize Flask application and WebSocket extension
app = Flask(__name__)
sock = Sock(app)

# Default route, displays Pac-Man
@app.route('/')
def index():
    # Render the index template
    return render_template('index.html')

# WebSocket route for sending data to the displayed page
@sock.route('/obci')
def obci(sock):
    # Connect to NeuroPype LSL output stream
    stream = resolve_stream('name', 'openbci_parsed')[0]
    inlet = StreamInlet(stream)

    # List of commands corresponding to JavaScript KeyBoardEvent key values
    commands = ['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp', 'Neutral']
    # Index of previously received command
    last_command = 4

    while True:
        # Collect a sample from the LSL stream and determine the index with the greatest value
        sample, _ = inlet.pull_sample()
        index = max(range(len(sample)), key=sample.__getitem__)

        # Only transmit directional commands if the previous command was neutral, and only transmit
        # neutral commands if the previous command was directional
        if (index == last_command):
            sock.send(commands[index])
        
        # Store the received command for use in the next loop iteration
        last_command = index

# If this module is being run directly, run the Flask application
if __name__ == '__main__':
    app.run(debug=True)