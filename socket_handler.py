from flask_socketio import SocketIO
from audio_processor import AudioProcessor
from speech2text import SpeechToText

class SocketHandler:
    def __init__(self, socketio: SocketIO, audio_processor: AudioProcessor, speech_to_text: SpeechToText):
        self.socketio = socketio
        self.audio_processor = audio_processor
        self.speech_to_text = speech_to_text

    def register_events(self):
        @self.socketio.on('audio_chunk')
        def handle_audio_chunk(audio_data):
            print('audio received in backend')
            processed_audio = self.audio_processor.process_audio(audio_data)
            
            # Do stuff with this audio
            text = self.speech_to_text.convert_to_text(processed_audio)

            print('speech to text ', text)

            location = query_location("")
            self.socketio.emit('location_pinpoint', location)

            # Do something with the text, e.g., query a location and emit back to client
            self.socketio.emit('converted_text', text)

def query_location(text):
    #dummy function to simulate querying location based on text
    return {"latitude": 40.7128, "longitude": -74.0060}