from flask_socketio import SocketIO

class Handler:
    def __init__(self, successor=None):
        self.successor = successor
    
    def handle_request(self, data):
        pass


class AudioProcessingHandler(Handler):
    def __init__(self, audio_processor, successor=None):
        super().__init__(successor)
        self.audio_processor = audio_processor

    def handle_request(self, data):
        processed_audio = self.audio_processor.process_audio(data)
        if self.successor:
            return self.successor.handle_request(processed_audio)

class SpeechToTextHandler(Handler):
    def __init__(self, stt_api, successor=None):
        super().__init__(successor)
        self.stt_api = stt_api

    def handle_request(self, data):
        text = self.stt_api.convert_to_text(data)
        if self.successor:
            return self.successor.handle_request(text)
        else:
            return text


class SocketEventListener:
    """ 
    SocketHandler handles the socket events using socketIO.

    Args:
        socketio (SocketIO): The Flask-SocketIO instance.
        audio_processor (AudioProcessor): The audio processor instance to handle audio data.
        speech_to_text (SpeechToText): The speech to text converter instance.
    """
    def __init__(self, socketio: SocketIO, first_handler: Handler):
        self.socketio = socketio
        self.first_handler = first_handler

    def register_events(self):
        """Register socket events."""
        @self.socketio.on('audio_chunk')
        def handle_audio_chunk(audio_data):
            """Handle the received audio chunk and emit the results.

            Args:
                audio_data (bytes): The received audio data.
            """
            try:
                transcription = self.first_handler.handle_request(audio_data)
                self.socketio.emit('transcription', transcription)
            except Exception as e:
                print(f"Error processing audio chunk: {e}")
