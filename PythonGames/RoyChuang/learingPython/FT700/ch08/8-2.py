import tkinter as tk

def click_func():               # 按鈕的自訂函式
    tkstr.set('被按了')        # 設定 tk 變數
#--↓主視窗↓--#
window = tk.Tk()                # 建立主視窗
window.geometry('340x100')
#--↓ Button ↓--#
tkstr = tk.StringVar()          # 建立 tk 變數
tkstr.set('請按我')              # 設定 tk 變數
btn = tk.Button(window, textvariable=tkstr,    # 建立按鈕元件
                font=('細明體', 20), 
                command=click_func)

btn.pack()                      # 排版設定
#'--↓啟動主視窗↓--#
window.mainloop()   