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

#--------↓ you-get 下載影片主程式 ↓---------#
url = 'https://www.youtube.com/watch?v=BKFLZVEiNH4'  # 影片網址
title, best = yget_info(url)	# 取得名稱與 itag
print(title, best)
r = yget_dl(url, best)	# 高品質下載
print('下載高品質:', 'OK' if r==0 else 'Error')  #傳回 0 表 OK
r = yget_dl(url)		# 預設品質下載
print('下載一般品質:', 'OK' if r==0 else 'Error')



