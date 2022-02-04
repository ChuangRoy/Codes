from utils import TONE
import numpy as np
from matplotlib import pyplot as plt
import sounddevice as sd
# from scipy.io.wavfile import write

# import threading

class Wave:
    def __init__(self, tone, length, tempo, fs):
    # Todo 0 請定義五個屬性:
    #       1. tone (音名，例如'A5', 'C4'等)
    #       2. length (節拍數)
    #       3. tempo (節拍)
    #       4. fs (取樣率)
    #       5. f (tone所對應到的頻率)
    # 前4個屬性為使用者輸入的
    # f則是從utils裡的TONE找尋

        self.tone = tone
        self.length = length
        self.tempo = tempo
        self.fs = fs
        self.f = TONE[tone]

        self.actived = np.zeros(length)
        self.setADSR()


    def sin_wave(self):
        # Todo 0 請依照定義的屬性生成對應的正弦波並回傳
        time_end = self.length*(60/self.tempo)

        # x = np.arange(0,time_end, (1/(self.fs-1)))
        # x = np.arange(0,time_end,1/self.fs)
        x = np.arange(len(self.energy()))/self.fs
        y = np.sin(2*np.pi*self.f*x)


        return y

    def press(self, idx):
        # Todo 1 請紀錄使用者按下的按鍵

        # if self.actived[idx] == 0:
        #     self.actived[idx] = 1
        # else:
        #     self.actived[idx] = 0

        self.actived[idx] = 1 - self.actived[idx]

    def square(self):
        # Todo 2 請依照Todo 2完成的紀錄生成對應的方波並回傳
        return np.repeat(self.actived, 60*self.fs/self.tempo)


    def envelope(self):
        # Todo 4 請生成envelope的波，你會需要定義ADSR
        duration_beat = 60/self.tempo

        attack = np.linspace(0,1, int(duration_beat*self.A*self.fs), False)
        decay = np.linspace(1,self.S, int(duration_beat*self.D*self.fs), False)
        sustain = np.linspace(self.S,self.S, int(duration_beat*(1-self.A-self.D)*self.fs), False)
        release = np.linspace(self.S,0, int(duration_beat*self.R*self.fs))

        envelope = np.concatenate((attack, decay, sustain, release), axis=None)

        return envelope

    def energy(self):
        # Todo 2 直接回傳self.square()即可
        # return self.square()

        # Todo 5 改以envelope()生成energy
        duration_beat = 60/self.tempo
        points_per_beat = int(self.fs*duration_beat)
        points_of_wave = self.length*points_per_beat + int(self.R*points_per_beat)

        energy = np.zeros(points_of_wave)

        envelope = self.envelope()

        for i in range(self.length):
            start = i*points_per_beat
            end = (i+1)*points_per_beat + int(self.R*points_per_beat)

            energy[start:end] = np.maximum(energy[start:end], self.actived[i]*envelope)

        return energy

    def export(self):
        # Todo 2 根據你完成的sin_wave()和energy()產生聲波並回傳
        return self.sin_wave()*self.energy()

        # Todo 6 產生聲波並回傳

    def setADSR(self, a=0.2, d=0.2, s=0.8, r=0.3):
        self.A = a
        self.D = d
        self.S = s
        self.R = r

    def plot(self):
        plt.subplot(5, 1, 1)
        y = self.sin_wave()
        x = np.arange(len(y))/self.fs
        plt.plot(x, y)
        plt.title("wave with frequency: " + str(self.f) + " (1/sec)")

        plt.subplot(5, 1, 2)
        y = self.square()
        x = np.arange(len(y))/self.fs
        plt.plot(x, y)
        plt.title("square")

        plt.subplot(5, 1, 3)
        y = self.envelope()
        x = np.arange(len(y))/self.fs
        plt.plot(x, y)
        plt.title("envelope")

        plt.subplot(5, 1, 4)
        y = self.energy()
        x = np.arange(len(y))/self.fs
        plt.plot(x, y)
        plt.title("energy")

        plt.subplot(5, 1, 5)
        y = self.export()
        x = np.arange(len(y))/self.fs
        plt.plot(x, y)
        plt.title("sound wave")

        plt.tight_layout()

        plt.show()


def play(wave, fs, volume=0.05):
    if(volume > 0.1): return

    sd.play((volume*wave), fs, blocking=True)

if __name__ == '__main__':
    test = Wave('C8', 8, 120, 48000)

    test.press(1)
    test.press(3)
    test.press(4)
    test.plot()


    # # Todo 3 建立多個Wave的實例並寫一段旋律，並使用play函式播放
    # # 播放時請一定要注意音量大小，不要傷到耳朵了
    C4 = Wave('C4', 8, 120, 48000)
    A4 = Wave('A4', 8, 120, 48000)

    C4.press(0)
    C4.press(1)
    A4.press(2)
    A4.press(3)
    C4.press(4)
    C4.press(5)

    # C4.plot()
    # A4.plot()

    music = C4.export() + A4.export()

    play(music, 48000)
