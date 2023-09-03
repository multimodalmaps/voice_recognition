import base64
class AudioProcessor:
    def process_audio(self, audio_data):
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        print("audo_base64:", audio_base64)

        payload = {
            "audio_base64": audio_base64,
            "format": "json"
        }
        # Process the audio data and return the processed audio
        # For now, just return the original audio_data
        return audio_data
