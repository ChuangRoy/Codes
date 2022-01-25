import ytube_module as m
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube  
import threading

#-------↓按紐事件的自訂函式↓------#
def click_func():
    url = yt_url.get()          # 取得文字輸入框的網址
    try:    #  測試 pytube 是否支援此網址或者網址是否正確
        YouTube(url)
    except:
        messagebox.showerror('錯誤','pytube 不支援此影片或者網址錯誤')   
        return
    #-----↓ 此 pytube 支援此網址, 進行網路爬蟲 ↓------#
    urls = m.get_urls(url)
    #------------↓ 輸入網址中有影片清單 ↓-----------------#
    if urls and messagebox.askyesno('確認方塊', 
            '是否下載清單內所有影片？(選擇 否(N) 則下載單一影片)') :       
    #--------↓ 下載清單中所有影片 ↓---------#
        print('開始下載清單')    
        for u in urls:     # 建立與啟動執行緒
            threading.Thread(target = m.start_dload, 
                             args=(u, listbox)).start()
    #--------↓ 下載單一影片 ↓---------#
    else:   
        yt = YouTube(url)   
        if messagebox.askyesno('確認方塊', 
                               f'是否下載{yt.title}影片？') :
            threading.Thread(target = m.start_dload, 
                             args=(url, listbox)).start()  
        else:
            print('取消下載')
#------------↓ 主視窗 ↓------------#
window = tk.Tk()                   # 建立主視窗物件
window.geometry('640x480')         # 主視窗尺寸
window.title('YouTube 極速下載器')  # 主視窗標題
#------------↓ Frame：上方輸入網址區域 ↓------------#
input_fm = tk.Frame(window, bg='red',   # 建立 Frame
                    width=640, height=120)
input_fm.pack()
#--↓ Label ↓--#
lb = tk.Label(input_fm, text='請輸入 YouTube 影片網址', 
              bg='red', fg='white',font=('細明體', 12))
lb.place(rely=0.25, relx=0.5, anchor='center')
#--↓ Entry ↓--#
yt_url = tk.StringVar()     # 用來取得使用者輸入的網址資料
entry = tk.Entry(input_fm, textvariable=yt_url, width=50)
entry.place(rely=0.5, relx=0.5, anchor='center')
#--↓ Button ↓--#
btn = tk.Button(input_fm, text='下載影片', command = click_func, 
                bg='#FFD700', fg='Black',font=('細明體', 10))
btn.place(rely=0.5, relx=0.85, anchor='center')
#------------↓ Frame：下方顯示下載清單區域 ↓------------#
dload_fm = tk.Frame(window, width=640, height=480-120)
dload_fm.pack()
#--↓ Label ↓--#
lb = tk.Label(dload_fm, text='下載狀態', 
              fg='black', font=('細明體', 10))
lb.place(rely=0.1, relx=0.5, anchor='center')
#--↓ Listbox ↓--#
listbox = tk.Listbox(dload_fm, width=65, height=15)
listbox.place(rely=0.5, relx=0.5, anchor='center')
#--↓ Scrollbar ↓--#
sbar = tk.Scrollbar(dload_fm)
sbar.place(rely=0.5, relx=0.87, anchor='center', relheight=0.7)
#--↓  List 與 Scrollbar 的連結 ↓--#
listbox.config(yscrollcommand = sbar.set)
sbar.config(command = listbox.yview)
#'--↓啟動主視窗↓--#
window.mainloop()