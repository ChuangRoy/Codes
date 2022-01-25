import tkinter as tk
#--↓主視窗↓--#
window = tk.Tk()                        # 建立主視窗
window.geometry('640x480')              # 設定尺寸為 640x480
window.title('YouTube 極速下載器')       # 設定主視窗標題
#--↓ Frame ↓--#
input_fm = tk.Frame(window, bg='red',   # 建立 Frame
                    width=640, height=120)
input_fm.pack() # 設定排版方式
#--↓啟動主視窗↓--#
window.mainloop()   