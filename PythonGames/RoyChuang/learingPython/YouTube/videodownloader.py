from pytube import YouTube
print("Youtube_Python下載工具")
print("製作人：莊鎮宇(s041516@apps.ntpc.edu.tw):D")
link=input('請輸入網址或輸入N結束操作：')
while link != "N" :
    print('努力下載中，請稍候....')
    yt=YouTube(link)
    video=yt.streams.filter(file_extension='mp4', res='720p').first()
    video.download()
    print("下載完畢")
    link=input('請輸入網址或輸入N結束操作：')


    