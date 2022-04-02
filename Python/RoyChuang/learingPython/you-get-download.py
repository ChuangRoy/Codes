import os
url = input('網址:')
try:
    os.system(f'you-get {url}')
except:
    os.system(f'you-get -debug {url}')