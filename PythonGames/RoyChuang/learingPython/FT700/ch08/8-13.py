from pytube import YouTube  # 匯入 Youtube 類別

url = 'https://www.youtube.com/watch?v=BKFLZVEiNH4'
yt = YouTube(url)
print('開始下載')
yt.streams.first().download()
print('下載完成')