import os
import openai


class SpeechToTextStrategy:
    def transcribe(self, audio_file_path: str) -> str:
        raise NotImplementedError

class WhisperStrategy(SpeechToTextStrategy):
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key
        
    def transcribe(self, audio_file_path: str) -> str:
        with open(audio_file_path, 'rb') as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
            print(response)
            self._clean_up_audio_file(audio_file_path)
        return response['text'] if 'text' in response else ''

    def _clean_up_audio_file(self, audio_file_path: str):
        try:
            os.remove(audio_file_path)
        except Exception as e:
            print(f"Error removing audio file: {e}")


class SpeechToTextWrapper:
    def __init__(self, strategy: SpeechToTextStrategy):
        self.strategy = strategy

    def convert_to_text(self, audio_file_path: str) -> str:
        return self.strategy.transcribe(audio_file_path)
    