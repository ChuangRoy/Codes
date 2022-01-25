import requests
from bs4 import BeautifulSoup
import os
import threading

def download_pic(url, path):
    pic = requests.get(url)     #使用 GET 對圖片連結發出請求
    path += url[url.rfind('.'):]     #將路徑加上圖片的副檔名   
    f = open(path,'wb')     #以指定的路徑建立一個檔案
    f.write(pic.content)     #將 HTTP Response 物件的 content寫入檔案中
    f.close()     #關閉檔案

def get_photolist(photo_name, download_num):    
    page = 1     #初始頁數為1
    photo_list = []     #建立空的圖片 list
    
    while True:
        url = 'https://pixabay.com/zh/photos/' + photo_name + '/?&pagi=' + str(page)
        #設定連結
        html = requests.get(url)     #GET請求
        html.encoding = 'utf-8'     #指定編碼為utf-8        
        bs = BeautifulSoup(html.text, 'lxml')     #解析網頁 
        photo_item = bs.find_all('div', {'class': 'item'})     
        #尋找所有標籤為 div, calss 為 'item' 的元素 
        if  len(photo_item) == 0:
            return None
        for i in range(len(photo_item)):
            photo = photo_item[i].find('img')['src']     
            #尋找標籤 img 並取出 'src' 之中的內容
            if photo in photo_list:
                return photo_list    
            if photo == '/static/img/blank.gif':
                photo = photo_item[i].find('img')['data-lazy']
                #尋找標籤 img 並取出 'data-lazy' 之中的內容
            photo_list.append(photo)     #將找到的連結新增進 list 之中
            if len(photo_list) >= download_num:
                return photo_list
        page+=1     #頁數加1
        
def create_folder(photo_name):
    folder_name = input("請輸入要儲存的資料夾名稱: ")
        
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在, 建立資料夾: " + folder_name)
    else:
        print("找到資料夾: " + folder_name)
            
    if not os.path.exists(folder_name + os.sep + photo_name):
        os.mkdir(folder_name + os.sep + photo_name)
        print("建立資料夾: " + photo_name)
    else:
        print(photo_name + " 資料夾已存在")
    return folder_name

def get_photobythread(folder_name, photo_name, photo_list):
    download_num = len(photo_list)     #設定下載數量為圖片連結串列的長度
    Q = int(download_num / 100)     #取商數
    R = download_num % 100     #取餘數 
    
    for i in range(Q):  
        threads = []  
        for j in range(100):
            threads.append(threading.Thread(target = download_pic, args = (photo_list[i*100+j], folder_name + os.sep + photo_name + os.sep + str(i*100+j+1))))
            threads[j].start()
        for j in threads:
            j.join()
        print(int((i+1)*100/download_num*100), '%')     #顯示當前進度
            
    threads = []
    for i in range(R):    
        threads.append(threading.Thread(target = download_pic, args = (photo_list[Q*100+i], folder_name + os.sep + photo_name + os.sep + str(Q*100+i+1))))               
        threads[i].start()               
    for i in threads:
        i.join()
    print("100%")     #顯示當前進度