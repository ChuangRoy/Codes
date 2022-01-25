from bs4 import BeautifulSoup
import requests
from pytube import YouTube  
def get_urls(url):  # 取得影片清單網址的自訂函式
    urls = []   # 影片清單網址
    if '&list=' not in url : return urls    # 單一影片
    response = requests.get(url)    # 發送 GET 請求
    if response.status_code != 200:
        print('請求失敗')
        return
    #-----↓ 請求成功, 解析網頁 ↓------#
    bs = BeautifulSoup(response.text, 'lxml')
    a_list = bs.find_all('a')
    base = 'https://www.youtube.com/'    # Youtube 主網址
    for a in a_list:
        href = a.get('href')
        url = base + href  # 主網址結合 href 才是完整的影片網址
        if ('&index=' in url) and (url not in urls):
            urls.append(url)
    return urls
#---------↓ 主程式 ↓---------#         
playlist_url = ('https://www.youtube.com/watch?v=BKFLZVEiNH4' 
                '&list=PLA5TE2ITfeXSn2f82Ek_YhhWF0pfkNHt2')
urls = get_urls(playlist_url)   #執行自訂函式
for url in urls:
    yt = YouTube(url)
    print(f'{yt.title}...下載中')
    yt.streams.first().download()
    print(f'{yt.title}...下載完成')