import base64
import io
import requests
import tempfile

class AudioProcessor:
    # def process_audio(self, audio_data):
    #     audio_base64 = base64.b64encode(audio_data).decode('utf-8')
    #     # print("audo_base64:", audio_base64)

    #     payload = {
    #         "audio_base64": audio_base64,
    #         "format": "json"
    #     }
    #     # Process the audio data and return the processed audio
    #     # For now, just return the original audio_data
    #     return audio_data

    def process_audio(self, audio_data):

        # Convert blob object to a file to feed to Whisper API
        def convertBlobToFile(blob):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(blob)
                print('audio file created ', tmp_file.name)
                return tmp_file.name

        audio_file = convertBlobToFile(audio_data)
        return audio_file

  
        
        
