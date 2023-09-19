# Voice Recognition Service

The `voice_recognition` module provides a comprehensive solution for processing and transcribing audio data. It leverages the Chain of Responsibility design pattern to ensure modularity and ease of extension.

## Features

- **Audio Processing**: Convert raw audio data into a suitable format for transcription.
- **Speech-to-Text**: Transcribe processed audio data into text.
- **Socket Handling**: Efficiently handle socket events and emit results using Flask-SocketIO.

## Installation

1. Clone the repository:
   ```bash
   git clone [repository_url]
   ```

git clone [repository_url]

cd voice_recognition

pip install -r requirements.txt

## Usage

1. Initialize the necessary components:

from audio_processor import AudioProcessor
from speech2text import SpeechToText
from socket_handler import SocketHandler

audio_processor = AudioProcessor()
speech_to_text = SpeechToText()

2. Set up the Chain of Responsibility:

speech_to_text_handler = SpeechToTextHandler(speech_to_text)
audio_processing_handler = AudioProcessingHandler(audio_processor, speech_to_text_handler)

3. Initialize the socket handler and register events:

socket_handler = SocketHandler(socketio, audio_processing_handler)
socket_handler.register_events()

4. Run the Flask application:

Run the Flask application:

## Extending the Module

Thanks to the Chain of Responsibility pattern, adding new processing steps or modifying existing ones is straightforward:

1. Create a new handler by extending the Handler base class.

2. Implement the handle_request method for the new handler.

3. Adjust the chain as needed by setting the new handler as a successor to an existing handler.
