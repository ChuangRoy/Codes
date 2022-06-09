import tkinter as tk
from tkinter import messagebox, ttk

class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python YouTube Video Downloader 影片下載器")
        self.window.geometry("500x600")
        self.window.resizable(0, 0)
        self.window.wm_attributes("-topmost", 1)
        print("製作人:RoyChuang")
        print("This is a python console這是一個Python主視窗")
        print("You can see all message here 你可以在這看到所有訊息")
        print("Please Don't close this window 請勿關閉此視窗")
        print("========================================================")
        # 顯示YouTube圖片
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # print(dir_path)
        self.Icon1 = tk.PhotoImage(file = dir_path + "\\" "YouTube_Icon_1.png")
        self.Image_Lable1 = tk.Label(self.window,image = self.Icon1)
        self.Image_Lable1.pack()
        # 設定網址輸入區域
        self.input_frm = tk.Frame(self.window, width=640, height=50)
        self.input_frm.pack()
        # 設定提示文字
        self.l1 = tk.Label(self.window, text="type URL here", font="none 12 bold")
        self.l1.pack()
        # 設定輸入框
        self.input_url = tk.StringVar()  # 取得輸入的網址
        self.input_et = tk.Entry(self.input_frm, textvariable=self.input_url, width=60)
        self.input_et.place(rely=0.75, relx=0.5, anchor='center')
        # 設定按鈕
        self.btn = tk.Button(self.input_frm, text='Download', command=self.click,
                        bg='orange', fg='Black')
        self.btn.place(rely=0.75, relx=0.9, anchor='center')



        self.dl_frm = tk.Frame(self.window, width=640, height=280)
        self.dl_frm.pack()


        # 下載清單
        self.lb = tk.Label(self.dl_frm, text='Download Message', font="none 12 bold")
        self.lb.place(rely=0.1, relx=0.5, anchor='center')

        self.listbox = tk.Listbox(self.dl_frm, width=65, height=15)
        self.listbox.place(rely=0.6, relx=0.5, anchor='center')
        self.sbar = tk.Scrollbar(self.dl_frm)
        self.sbar.place(rely=0.6, relx=0.87, anchor='center', relheight=0.75)
        self.listbox.config(yscrollcommand=self.sbar.set)

        # l1 = tk.Label(window, text="Made by Roy Chuang ！ s041516@apps.ntpc.edu.tw",  font="none 12 bold")
        # l1.pack()

        self.listbox.insert(tk.END, '製作人:RoyChuang')
        self.listbox.insert(tk.END, '開發工具:Python')
        self.listbox.insert(tk.END, '開發模組:Urllib3,youtube-dl,tkinter,threading')
        self.listbox.insert(tk.END, '注意:影片下載完成前，可能產生不完整(下載到一半)影片檔，請勿開啟')
        self.listbox.insert(tk.END, '注意:如中途網路中斷或關閉程式可能殘留未完成影片檔，將其刪除即可')
        self.listbox.insert(tk.END, '----------------------------------------------------------------------------------')
    def insert_text(self, words):
        self.listbox.insert(tk.END, words)

    def click(self):
        self.download()

    def download(self):
        print("下載影片")
    def download_ask(self):
        print("下載影片")
        download_playlist = messagebox.askquestion("是否下載播放清單","是否下載播放清單")
        return download_playlist=="yes"

    def no_url(self):
        messagebox.showerror("請檢察網址是否正確或網路連線是否正常","請檢察網址是否正確或網路連線是否正常")

    def mainloop(self):
        self.window.mainloop()

def main():
    gui = Window()
    gui.window.mainloop()

if __name__ == "__main__":
    main()
