import tkinter as tk
#--↓建立主視窗↓--#
window = tk.Tk()                # 建立主視窗
#--↓ Listbox 列表框↓--#
listbox = tk.Listbox(window)    # 建立列表框
print(f'資料筆數：{listbox.size()}')
for row in range(30):
   listbox.insert(tk.END, f'第 {row} 筆資料')  # 從尾端插入 30 筆資料
print(f'資料筆數：{listbox.size()}') 
listbox.pack()
#--↓啟動主視窗↓--#
window.mainloop()