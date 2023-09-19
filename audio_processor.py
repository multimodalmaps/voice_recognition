import tempfile

class AudioProcessor:
    '''AudioProcessor class to process audio data.'''
    
    def process_audio(self, audio_data: bytes) -> str:
        """Convert the given audio data to a temporary WAV file.

        Args:
            audio_data (bytes): The audio data to be processed.

        Returns:
            str: The path to the temporary audio file.
        """
        return self._convert_blob_to_file(audio_data)

    def _convert_blob_to_file(self, blob: bytes) -> str:
        """Convert the given blob data to a temporary WAV file.

        Args:
            blob (bytes): The blob data to be converted.

        Returns:
            str: The path to the temporary WAV file.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(blob)
            print(f'Audio file created at {tmp_file.name}')
            return tmp_file.name
