from urllib.request import urlopen
import threading
from sys import exit

def Check_Url(url):
    try:
        print("")
        print("檢查網址")
        # threading.Thread(target=urlopen(url)).start()
        urlopen(url)
    except:
        return False
    else :
        print("網址正確")
        return True    
    exit()

if __name__ == "__main__":
    URL = input("URL:")
    URL_Exist = Check_Url(URL)
    if URL_Exist == True:
        print("URL Exist")
    else :
        print("URL Isn't Exist")
        