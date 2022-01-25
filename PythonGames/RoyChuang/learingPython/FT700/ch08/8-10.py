import tkinter as tk
#--↓主視窗↓--#
window = tk.Tk()
#--↓ Button ↓--#
n = 0
for r in range(2):
    for c in range(3):
        btn = tk.Button(window, text=f'No.{n}', width=20)
        btn.grid(row=r, column=c, padx=5, pady=10)
        n+=1
#'--↓啟動主視窗↓--#
window.mainloop()