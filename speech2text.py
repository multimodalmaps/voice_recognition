import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print('api key', openai.api_key)


class SpeechToText:
    def convert_to_text(self, processed_audio):

        def transcribe_audio(audio_filepath):
            with open(audio_filepath, 'rb') as audio_file:
                response = openai.Audio.transcribe("whisper-1", audio_file)
                print(response)
            
            # Delete the temporary file
            os.remove(audio_filepath)
            
            return response['text']

        # Implement this later
        # response = requests.post("https://api.openai.com/v1/whisper/asr", headers=headers, json=payload)

        # if response.status_docde == 200:
        #     text = response.json().get("transcription", "")

        #     #do something with the text
        #     location = query_location(text)

        #     socketio.emit('location_pinpoint', location)
        # else:
        #     print(f"Whisper API error: {response.content}")


        # Convert the processed audio to text
        # For now, return a dummy string
        text = transcribe_audio(processed_audio)
        return text
    
    
