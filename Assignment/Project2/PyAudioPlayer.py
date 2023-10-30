from pyaudio import PyAudio, Stream

from Assignment.Project2.decorator.NotNone import NotNone
from Assignment.Project2.wrapper.AudioManager import AudioManager
from Assignment.Project2.wrapper.LoadedAudioFile import LoadedAudioFile
from matplotlib.pyplot import xlabel, ylabel, title, show
from librosa.display import waveshow
from typing import Optional
from concurrent.futures import ProcessPoolExecutor
from asyncio import Task, create_task, sleep, run, to_thread, get_event_loop, AbstractEventLoop
from threading import Thread

import asyncio
import os


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class PyAudioPlayer:
    def __init__(self):
        self._audio_source_dir = os.path.join(ROOT_PATH, "audio_sources")
        self._loaded_file: Optional[LoadedAudioFile] = None
        self._audio_manager: Optional[AudioManager] = None
        self._is_playing: bool = False
        asyncio.run(self._menu())

    def _load(self):
        input_audio_file_dir = os.path.join(self._audio_source_dir, input("input filename? : "))
        self._loaded_file = LoadedAudioFile.create_object(wav_file_dir = input_audio_file_dir)

        print("Sampling rate = " + self._loaded_file.sampling_with_format())

        print("Play time = " + self._loaded_file.length_with_format())

    @NotNone("_loaded_file")
    async def _plot(self):
        signal = self._loaded_file.librosa.signal
        sampling_rate = self._loaded_file.librosa.sampling_rate

        start_time = int(int(input("start time ? :")) * sampling_rate)
        end_time = int(int(input("end time ? :")) * sampling_rate)

        waveshow(signal[start_time:end_time], sr=sampling_rate)
        xlabel("Time (s)")
        ylabel("Amplitude")
        title("Audio Segment")
        show()

    @NotNone("_loaded_file")
    async def _play(self):
        audio_manager = AudioManager.create_manager(loaded_audio_file=self._loaded_file)
        audio_thread = Thread(target = audio_manager.play)
        audio_thread.start()
        self._audio_manager = audio_manager

    @NotNone("_audio_manager")
    async def _stop(self):
        self._audio_manager.stop()

    async def _menu(self):
        while True:
            input_command = input("1. Load, 2. Play, 3. Stop, 4. R-Play, 5. Plot, 6. Exit ? ")
            try:
                if input_command == "1":
                    self._load()

                elif input_command == "2":
                    await self._play()

                elif input_command == "3":
                    await self._stop()
                #
                # elif input_command == "4":
                #     self._r_play()

                elif input_command == "5":
                    await self._plot()

                elif input_command == "6":
                    break

                else:
                    print("입력값이 잘못되었습니다. 다시 입력하십시오.")

            except Exception as e:
                print(e)


if __name__ == '__main__':
    PAP = PyAudioPlayer()

