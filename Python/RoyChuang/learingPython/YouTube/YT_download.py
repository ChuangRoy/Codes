import tkinter as tk
from tkinter import messagebox, ttk
from pytube import YouTube
import threading


def click():
    def download():
            try:
                url = input_url.get()
                yt = YouTube(url)
                title = yt.title
            except:
                listbox.insert(tk.END, '請檢察網路連線或網址錯誤')
                print("請檢察網路連線或網址錯誤" )
            else:
                try:
                    listbox.insert(tk.END, '%s............努力下載中，請稍候'%yt.title)
                    print("%s.........努力下載中，請稍候" % yt.title)
                    video = yt.streams.filter(file_extension='mp4',
                                              res='%s' % cbb.get()).first()
                    video.download()
                except:
                    listbox.insert(tk.END, '%s...請檢察是否支援此畫質或網路中斷'%yt.title)
                    print('%s...請檢察是否支援此畫質或網路中斷'%yt.title)
                else:
                    print("%s.........下載完畢" %yt.title)
                    listbox.insert(tk.END, '%s.....下載完畢'%yt.title)
    threading.Thread(target = download).start()
    
    



    
    

window = tk.Tk()
window.title("Python YouTube Video Downloader 影片下載器")
window.geometry("500x500")
window.resizable(0,0)
window.wm_attributes("-topmost",1)
#window.iconbitmap('YT.ico') 
print("製作人:莊鎮宇 s041516@apps.ntpc.edu.tw")
print("This is a python console這是一個Python主視窗")
print("You can see all message here 你可以在這看到所有訊息")
print("Please Don't close this window 請勿關閉此視窗")
print("=====================================================================================")

#設定網址輸入區域
input_frm = tk.Frame(window, width=640, height=50)
input_frm.pack()
#設定提示文字
l1 = tk.Label(window, text="type URL here",  font="none 12 bold")
l1.pack()
#設定輸入框
input_url = tk.StringVar()     # 取得輸入的網址
input_et = tk.Entry(input_frm, textvariable=input_url, width=60)
input_et.place(rely=0.75, relx=0.5, anchor='center')
#設定按鈕

btn = tk.Button(input_frm, text='Download', command = click,
                bg='orange', fg='Black')
btn.place(rely=0.75, relx=0.9, anchor='center')


choice_frm = tk.Frame(window, width=640, height=50)
choice_frm.pack()

lb = tk.Label(choice_frm, text='Quality品質 :',
              fg='black')
lb.place(rely=0.2, relx=0.1)


def callbackFunc(event):
    listbox.insert(tk.END, 'Selected'+cbb.get())

cbb = ttk.Combobox(choice_frm,
                   values=[
                       "720p",
                       "480p",
                       "360p"], state="readonly", width=12)

cbb.place(rely=0.2, relx=0.3)
cbb.current(0)

cbb.bind("<<ComboboxSelected>>", callbackFunc)



dl_frm = tk.Frame(window, width=640, height=280)
dl_frm.pack()


lb = tk.Label(dl_frm, text='Download Message', font="none 12 bold")
lb.place(rely=0.1, relx=0.5, anchor='center')



listbox = tk.Listbox(dl_frm, width=65, height=15)
listbox.place(rely=0.6, relx=0.5, anchor='center')
sbar = tk.Scrollbar(dl_frm)
sbar.place(rely=0.6, relx=0.87, anchor='center', relheight=0.75)
listbox.config(yscrollcommand=sbar.set)


 #l1 = tk.Label(window, text="Made by Roy Chuang ！ s041516@apps.ntpc.edu.tw",  font="none 12 bold")
 #l1.pack()
listbox.insert(tk.END, '製作人:莊鎮宇 ！ s041516@apps.ntpc.edu.tw')
listbox.insert(tk.END, '開發工具:Python,Pyinstaller')
listbox.insert(tk.END, '開發模組:Pytube,tkinter,threading')
listbox.insert(tk.END, '新功能:同時下載多個影片檔')
listbox.insert(tk.END, '注意:影片下載完成前，可能產生不完整(下載到一半)影片檔，請勿開啟')
listbox.insert(tk.END, '注意:如中途網路中斷或關閉程式可能殘留未完成影片檔，將其刪除即可')
listbox.insert(tk.END, '即將推出下載播放清單功能，敬請期待')
listbox.insert(tk.END, '----------------------------------------------------------------------------------')
window.mainloop()
