import ytube_module as m   # 匯入自訂模組
from pytube import YouTube
import threading

lock = threading.Lock()     # 建立鎖物件
def start_dload(url, listbox):       # 下載影片的多執行緒工作函式
    try:
        yt = YouTube(url)
    except:
        print('pytube 不支援此影片或者網址錯誤')
        return
    name = yt.title
    #---------------↓ 鎖定區域 A ↓---------------#
    lock.acquire()              # 進行鎖定
    print(f'{name}.....下載中')
    lock.release()              # 釋放鎖定
    #---------------↑ 鎖定區域 A ↑---------------#
    yt.streams.first().download()   # 開始下載影片 (不需要鎖定)
    #---------------↓ 鎖定區域 B ↓---------------#
    lock.acquire()              # 進行鎖定
    print(f'●{name}.....下載完成')
    lock.release()              # 釋放鎖定
    #---------------↑ 鎖定區域 B ↑---------------#
#---------↓ 主程式 ↓---------#
url = ('https://www.youtube.com/watch?v=BKFLZVEiNH4'
       '&list=PLA5TE2ITfeXSn2f82Ek_YhhWF0pfkNHt2')
urls = m.get_urls(url)   # 取回影片清單
if urls:
    for u in urls:
        threading.Thread(target = start_dload,  # 建立執行緒進行下載
                         args=(u,'Listbox')).start()
else:
    print('此網址為單一影片')
    threading.Thread(target = start_dload,      # 建立執行緒進行下載
                     args=(url,'Listbox')).start()