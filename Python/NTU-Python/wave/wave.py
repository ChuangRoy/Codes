from utils import TONE
import numpy as np
# import math
from matplotlib import pyplot as plt
# import sounddevice as sd

# from scipy.io.wavfile import write

class Wave:
    def __init__(self, tone, length, tempo, fs):
    # Todo 0 請定義四個屬性:
    #       1. tone (音名，例如'A5', 'C4'等)
    #       2. length (節拍數)
    #       3. tempo (節拍)
    #       4. fs (取樣率)
    #       5. f (tone所對應到的頻率)s
    # 前4個屬性為使用者輸入的
    # f則是從utils裡的TONE找尋
        self.tone = tone
        self.length = length
        self.tempo = tempo
        self.fs = fs
        self.f = TONE[tone]

        self.activate = np.zeros(length)

    def sin_wave(self):
        # Todo 0 請依照定義的屬性生成對應的正弦波並回傳
        # time_start = 0
        # time_end = int(self.length*(60/self.tempo))
        # sample_count = time_end*self.fs

        # x = list(range(sample_count))
        # for idx,t in enumerate(x):
        # 	x[idx] = (t/sample_count)*time_end

        # y = []
        # for t in x:
        # 	y.append(math.sin(2*math.pi*self.f*t))

        # return y

       time_end = self.length*(60/self.tempo)

       x = np.arange(0,time_end, (1/(self.fs-1)))
       x = np.arange(len(self.energy()))
       y = np.sin(2*np.pi*self.f*x)

       return y


    def press(self, idx):
        # Todo 1 請紀錄使用者按下的按鍵
    	self.activate[idx] = 1 - self.activate[idx]

    def square(self):
        # Todo 2 請依照Todo 2完成的紀錄生成對應的方波並回傳
        return np.repeat(self.activate, 60*self.fs/self.tempo)

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
        return self.square()

        # Todo 5 改以envelope()生成energy

    def export(self):
        # Todo 2 根據你完成的sin_wave()和energy()產生聲波並回傳

        # Todo 6 產生聲波並回傳
   	    return self.sin_wave()*self.energy() #bug!!!

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


# def play(wave, fs, volume=0.05):
#     if(volume > 0.1): return

#     sd.play((volume*wave), fs, blocking=True)

if __name__ == '__main__':
    # Todo 3 建立多個Wave的實例並寫一段旋律，並使用play函式播放
    # 播放時請一定要注意音量大小，不要傷到耳朵了
    wave = Wave("C4", 4, 4, 1000)

    wave.press(1)
    wave.press(2)
    wave.press(3)

    wave.plot()
