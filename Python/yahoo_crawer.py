from urllib.request import urlopen
from bs4 import BeautifulSoup
url = urlopen("https://tw.yahoo.com/")
bs = BeautifulSoup(url)
print(bs)
import os
os.system("pause")