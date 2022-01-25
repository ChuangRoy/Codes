import tkinter as tk
#--↓建立主視窗↓--#
window = tk.Tk()                
#--↓Listbox 列表框↓--#
listbox = tk.Listbox(window)
for row in range(30):
   listbox.insert(tk.END, f'第 {row} 筆資料')
listbox.pack(side = tk.LEFT)
#--↓Scrollbar 捲動軸↓--#
sbar = tk.Scrollbar(window)     # 建立捲動軸
sbar.pack(side = tk.RIGHT, fill = tk.Y)
#--↓列表框與捲動軸的連結↓--#
sbar.config(command = listbox.yview)  
listbox.config(yscrollcommand = sbar.set)
#--↓啟動主視窗↓--#
window.mainloop()
