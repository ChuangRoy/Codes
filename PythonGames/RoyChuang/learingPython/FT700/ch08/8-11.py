import tkinter as tk
#--↓主視窗↓--#
window = tk.Tk()
window.geometry('400x200')    # 設定尺寸為 640x480
#--↓ Button ↓--#
n = 0
for w in range(0, 100, 25):
    for h in range(0, 100, 25):
        btn = tk.Button(window, text=f'No.{n}', 
                        width=10, height=2)
        btn.place(relx=w/100, rely=h/100)
        n+=1
#'--↓啟動主視窗↓--#
window.mainloop()