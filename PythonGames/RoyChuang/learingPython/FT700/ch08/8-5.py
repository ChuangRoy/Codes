import tkinter as tk

def check_pw():
    if pwvar.get() == 'flag':
        msgvar.set('密碼正確')
    else:
        msgvar.set('密碼錯誤')
#--↓主視窗↓--#
window = tk.Tk() # 建立主視窗
#--↓Label：提示輸入密碼 ↓--#
lb_pw = tk.Label(window, text='輸入密碼')    # 建立 Label
lb_pw.pack()    
#--↓Entry：密碼的輸入文字框↓--#
pwvar = tk.StringVar()                      # 建立 tk 字串變數
entry = tk.Entry(window, width=15,          # 建立文字輸入框
                 textvariable=pwvar,
                 show='*')
entry.pack()    
#--↓Button：驗證密碼是否正確↓--#
btn = tk.Button(window, text='驗證',   # 建立 Button 元件
                command=check_pw)
btn.pack()
#--↓Label：提示是否輸入正確↓--#
msgvar = tk.StringVar()                     # 建立 tk 字串變數
lb_msg = tk.Label(window, textvariable=msgvar)  # 建立 Label
lb_msg.pack()
#--↓啟動主視窗↓--#
window.mainloop()