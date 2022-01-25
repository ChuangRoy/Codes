import tkinter as tk
#--↓主視窗↓--#
window = tk.Tk()                    # 建立主視窗
window.title('YouTube 極速下載器')   # 設定主視窗標題
#--↓ Label ↓--#
lb = tk.Label(window, 
              bg='red', fg='white',
              text='請輸入 YouTube 網址',
              font=('細明體', 30), padx=50, pady=80)
lb.pack()
#--↓啟動主視窗↓--#
window.mainloop()   