from typing import Optional
from pyaudio import PyAudio, Stream

from Assignment.Project2.wrapper.LoadedAudioFile import LoadedAudioFile


class AudioManager(PyAudio):
    def __init__(self, loaded_audio_file: LoadedAudioFile):
        super().__init__()
        self._loaded_audio_file: LoadedAudioFile = loaded_audio_file
        self._audio_stream: Stream = self._create_audio_stream()

    def _create_audio_stream(self) -> Stream:
        return self.open(
            format = self.get_format_from_width(self._loaded_audio_file.file.getsampwidth()),
            channels = self._loaded_audio_file.file.getnchannels(),
            rate = self._loaded_audio_file.file.getframerate(),
            output = True
        )

    def play(self):
        while len(audio_data := self._loaded_audio_file.file.readframes(1024)):
            self._audio_stream.write(audio_data)

        self.stop()

    def stop(self):
        self._audio_stream.close()
        self._audio_stream = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._audio_stream is not None:
            self.stop()

        self.terminate()
        pass



