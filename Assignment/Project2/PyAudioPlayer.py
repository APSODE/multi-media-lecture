from typing import Optional
from librosa import load

from pyaudio import PyAudio
from wave import open as wv_open
from wave import Wave_read, Wave_write


import os
import matplotlib.pyplot as plt
import librosa

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


# Wave_read 객체에 대한 wrapper클래스
class _LoadedAudioFile:
    def __init__(self, wav_file_dir: str):
        self._wav_file = wv_open(wav_file_dir, "rb")
        self._librosa_tuple = load(wav_file_dir)
        self._length = round(self._wav_file.getnframes() / self._wav_file.getframerate(), 2)

    @staticmethod
    def create_object(wav_file_dir: str) -> "_LoadedAudioFile":
        return _LoadedAudioFile(wav_file_dir = wav_file_dir)

    @property
    def file(self) -> Wave_read:
        return self._wav_file

    @property
    def length(self) -> float:
        return self._length
    
    @property
    def sampling(self) -> float:
        return self._wav_file.getframerate() / 1000

    @property
    def librosa_tuple(self) -> tuple:
        return self._librosa_tuple

    def length_with_format(self) -> str:
        minute = int(self._length // 60)
        second = int(self._length - (60 * minute))

        return f"{minute}분 {second}초"

    def sampling_with_format(self):
        return f"{self._wav_file.getframerate() / 1000}KHz"


class PyAudioPlayer(PyAudio):
    def __init__(self):
        super().__init__()
        self._audio_source_dir = os.path.join(ROOT_PATH, "audio_sources")
        self._loaded_file: Optional[_LoadedAudioFile] = None
        self._dir_checker()
        self.run()

    def run(self):
        self._menu()

    def _load(self):
        input_audio_file_dir = os.path.join(self._audio_source_dir, input("input filename? : "))
        self._loaded_file = _LoadedAudioFile.create_object(wav_file_dir = input_audio_file_dir)

        print("Sampling rate = " + self._loaded_file.sampling_with_format())
        print("Play time = " + self._loaded_file.length_with_format())

    def _play(self):
        pass

    def _stop(self):
        pass

    def _r_play(self):
        pass

    def _plot(self):
        y = self._loaded_file.librosa_tuple[0]
        sr = self._loaded_file.librosa_tuple[1]

        start_time = int(int(input("start time ? :")) * sr)
        end_time = int(int(input("end time ? :")) * sr)

        sliced_y = y[start_time:end_time]
        # waveshow 함수가 matplotlib의 변경으로 인해 librosa의 현재 릴리즈 버전에서는
        # matplotlib 3.8이상의 버전을 사용하면 예외가 발생한다.
        # 따라서 matplotlib 3.7.3을 사용할 경우 정상적으로 출력이 가능한 것을 확인함.
        librosa.display.waveshow(sliced_y, sr = sr)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title("Audio Segment")
        plt.show()

    def _dir_checker(self):
        if not os.path.exists(self._audio_source_dir):
            os.mkdir(self._audio_source_dir)

    def _menu(self):
        while True:
            input_command = input("1. Load, 2. Play, 3. Stop, 4. R-Play, 5. Plot, 6. Exit ? ")
            if input_command == "1":
                self._load()

            elif input_command == "2":
                self._play()

            elif input_command == "3":
                self._stop()

            elif input_command == "4":
                self._r_play()

            elif input_command == "5":
                self._plot()

            elif input_command == "6":
                # break
                pass

            else:
                print("입력값이 잘못되었습니다. 다시 입력하십시오.")


if __name__ == '__main__':
    PAP = PyAudioPlayer()
