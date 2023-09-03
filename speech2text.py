import openai

open_ai_api_key = "OPEN_AI_API_KEY"

headers = {
    'Authorization': f"Bearer {open_ai_api_key}",
    'Content-Type': 'application/json'
}

class SpeechToText:
    def convert_to_text(self, processed_audio):
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
        return "This is converted text."
    
    def transcribe_audio(audio_file_path):
        with open(audio_file_path, 'rb') as audio_file:
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
        return transcription['text']
