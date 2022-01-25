import tkinter as tk
from tkinter import messagebox

def hello():
   messagebox.askyesno('提問對話框', '你好嗎？')
   
window = tk.Tk()
btn = tk.Button(window, text ='按鈕', command = hello)
btn.pack()
window.mainloop()