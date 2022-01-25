import ytubeX_module as m
import tkinter as tk
from tkinter import messagebox
import threading

#-------↓按紐事件的自訂函式↓------#
def click_func():
    url = yt_url.get()      # 取得文字輸入框的網址
    if url.strip() == '': return   # 如果為空字串就結束函式
    urls = m.get_urls(url)  # 進行網路爬蟲, 尋找是否有播放清單
    if urls:   #←有播放清單
        if messagebox.askyesno('確認方塊',
                      '是否下載清單內所有影片？(選擇 否(N) 則下載單一影片)'):
            threading.Thread(target = multi_dload,    #←下載清單中所有影片
                             args=(urls, listbox)).start()
        else:
            threading.Thread(target = m.start_dload,  #←下載單一影片
                             args=(url, listbox)).start()
    else:     #←沒有播放清單, 直接下載
            threading.Thread(target = m.start_dload,
                             args=(url, listbox)).start()

import re  #下面函式在排序播放清單中的項目時會用到 re 模組
def multi_dload(urls, listbox):
    max_thread = threading.activeCount() + 20   #←計算開啟執行緒的數量上
    urls.sort(key = lambda s: int(re.search('index=\d+', s).group()[6:])) #←將清單排序 (詳情後述)
    for url in urls:     # 建立與啟動執行緒
        while threading.activeCount() >= max_thread:
            pass
        threading.Thread(target = m.start_dload,
                         args=(url, listbox)).start()

#------------↓ 主視窗 ↓------------#
window = tk.Tk()              # 建立主視窗物件
listbox, yt_url = m.build_window(window, click_func)
window.mainloop()