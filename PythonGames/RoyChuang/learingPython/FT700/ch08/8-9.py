import tkinter as tk
#--↓主視窗↓--#
window = tk.Tk()
#--↓ Button ↓--#
for n in range(3):
    btn = tk.Button(window, text=f'No.{n}', width=20)
    btn.pack(side=tk.LEFT, padx=30, pady=40, fill=tk.X)
#'--↓啟動主視窗↓--#
window.mainloop()