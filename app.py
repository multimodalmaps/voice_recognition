from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO
from audio_processor import AudioProcessor  # Import the new module
from speech2text import SpeechToText  # Import the new module
from socket_handler import SocketHandler

app = Flask(__name__)
CORS(app)  # Handle CORS
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    audio_processor = AudioProcessor()  # Initialize the new module
    speech_to_text = SpeechToText()  # Initialize the new module
    socket_handler = SocketHandler(socketio, audio_processor, speech_to_text)  # Pass the new modules as arguments
    socket_handler.register_events()
    socketio.run(app,port=5001)