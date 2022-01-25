from bs4 import BeautifulSoup
import requests
import threading
from pytube import YouTube
import tkinter as tk

def get_urls(url):
    urls = []   # 影片清單網址
    if '&list=' not in url : return urls    # 單一影片
    response = requests.get(url)    # 發送 GET 請求
    if response.status_code != 200:
        print('請求失敗')
        return
    #-----↓ 請求成功 ↓------#
    bs = BeautifulSoup(response.text, 'lxml')
    a_list = bs.find_all('a')
    base = 'https://www.youtube.com/'        # Youtube 開頭網址
    for a in a_list:
        href = a.get('href')
        url = base + href
        if ('&index=' in url) and (url not in urls):
            urls.append(url)
    return urls

# 下載清單影片的多執行緒函式 threading job
lock = threading.Lock()
def start_dload(url, listbox):
    yt = YouTube(url)
    name = yt.title
    #---------------↓ 鎖定區域 A ↓---------------#
    lock.acquire()              # 進行鎖定
    no = listbox.size()     # 以目前列表框筆數為下載編號
    listbox.insert(tk.END, f'{no:02d}:{name}.....下載中')
    print('插入:', no, name)
    lock.release()              # 釋放鎖定
    #---------------↑ 鎖定區域 A ↑---------------#
    yt.streams.first().download()   # 開始下載影片 (不可鎖定)
    #---------------↓ 鎖定區域 B ↓---------------#
    lock.acquire()              # 進行鎖定
    print('更新:', no, name)
    listbox.delete(no)
    listbox.insert(no, f'{no:02d}:●{name}.....下載完成')
    lock.release()              # 釋放鎖定
    #---------------↑ 鎖定區域 B ↑---------------#
    