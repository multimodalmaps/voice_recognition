import os
# from dotenv import load_dotenv

# load_dotenv()

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from audio_processor import AudioProcessor
from speech2text import SpeechToTextWrapper, WhisperStrategy
from socket_handler import AudioProcessingHandler, SpeechToTextHandler, SocketEventListener

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins":  "https://multimodalmap-frontend.s3.us-west-2.amazonaws.com/index.html"}})
socketio = SocketIO(app, cors_allowed_origins=["http://localhost:3000", "https://multimodalmap-frontend.s3.us-west-2.amazonaws.com/index.html"])

# api_key = os.getenv("OPENAI_API_KEY")
api_key = os.environ["OPENAI_API_KEY"]
print(api_key) 

@app.route('/')
def dummy_route():
    return 'Working!'

audio_processor = AudioProcessor()
whisper_stt = SpeechToTextWrapper(WhisperStrategy(api_key))

speech_to_text_handler = SpeechToTextHandler(stt_api=whisper_stt)
audio_processing_handler = AudioProcessingHandler(audio_processor, successor=speech_to_text_handler)

socket_event_listener = SocketEventListener(socketio, first_handler=audio_processing_handler)
socket_event_listener.register_events()


# if __name__ == '__main__':
#     socketio.run(app, port=8000)
