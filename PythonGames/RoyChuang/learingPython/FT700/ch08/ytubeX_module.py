from bs4 import BeautifulSoup
import requests
import threading
from pytube import YouTube
import tkinter as tk

def build_window(window, click_func):  # 建置視窗的內容
    window.geometry('640x480')         # 主視窗尺寸
    window.title('YouTube 極速下載器 (火力加強版)')  # 主視窗標題
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
    return listbox, yt_url

def get_urls(url):  # 解析網頁中的播放清單
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

lock = threading.Lock()
def set_listbox(listbox, pos, msg):
    lock.acquire()              # 進行鎖定
    if pos < 0:  #←新增項目
        pos = listbox.size()    # 以目前列表框筆數為下載編號
        listbox.insert(tk.END, f'{pos+1:02d}:' + msg)
    else:        #←更改項目內容
        listbox.delete(pos)
        listbox.insert(pos, f'{pos+1:02d}:' + msg)
    lock.release()              # 釋放鎖定
    return pos

# 下載影片的多執行緒函式
def start_dload(url, listbox):
    no = set_listbox(listbox, -1, f'讀取 {url}')  #新增 listbox 項目
    title, best = yget_info(url)  #←先使用 you-get 讀取資訊
    if title == '': #←you-get 無法讀取, 改用 pytube 讀取
        try:    # 用 try 測試 pytube 是否可以讀取影片資訊
            yt = YouTube(url)
            title = yt.title + ' ' #加一空格以和 you-get 訊息有所分別
            best = ''   #←設為空字串表示可用 pytube 下載
        except:  #←pytube 讀取失敗
            pass   # pass 表示什麼也不做

    if title == '':  #←如果為空字串表示 pytube 和 you-get 都無法下載
        name = '▲影片無法讀取 (設為私人影片、已刪除、或網址錯誤)'
    else:  #←否則顯示下載中
        name =  f'○{title}...下載中'
    set_listbox(listbox, no, name)   #更改 listbox 第 no 項的內容

    if title == '': #←為空字串表示 pytube 和 you-get 都無法下載
        return     # 結束函式
    if best:   #←best 不是空字串就表示可用 you-get 下載
        yget_dl(url)        # 開始下載預設的影片 (不可鎖定)
    else:    #←否則使用 pytube 下載
        yt.streams.first().download()   # 開始下載影片 (不可鎖定)
    set_listbox(listbox, no, f'●{title}...下載完成')  #更改 listbox

#-----↓ you-get 查詢影片資訊及下載函式 ↓-----
import subprocess as sp  # 更名為較簡短的 sp

def yget_info(url):
    process = sp.Popen('you-get -i ' + url,
                       shell=True,
                       stdout=sp.PIPE, stderr=sp.PIPE)
    r = process.communicate()
    s = str(r[0], 'utf-8')
    if s.find('title:') < 0:  # 搜不到 title: 則視為失敗
        return '', ''
    title = s[s.find('title:')+6: s.find('streams')].strip()
    itag  = s[s.find('itag:')+6: s.find('container')].strip()
    if len(itag) > 8:   #如果 itag0 內容有 ESC 資料(例 b'\x1b[7m137\x1b[0m')
        itag = itag[4:-4]  #去除、前後4個 ESC 字元
    return title, itag  #↑傳回 title 為空字串時表示讀取失敗

#--------↓ you-get 下載影片自訂函式 ↓---------#
def yget_dl(url, itag = None):
    cmd = 'you-get '
    if itag:
        cmd = cmd + '--itag=' + itag + ' '
    process = sp.Popen(cmd + url)
    process.wait()
    return process.returncode  #傳回 0 表 OK
