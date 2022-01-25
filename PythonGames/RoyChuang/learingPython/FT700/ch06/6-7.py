import requests      # 匯入 requests 套件

def send_ifttt(v1, v2, v3):   # 定義函式來向 IFTTT 發送 HTTP 要求
    url = ('https://maker.ifttt.com/trigger/toline/with/' +
          'key/ckyTQ8zoYfDiJgha830XbL' +
          '?value1='+str(v1) +
          '&value2='+str(v2) +
          '&value3='+str(v3))
    r = requests.get(url)      # 送出 HTTP GET 並取得網站的回應資料
    if r.text[:5] == 'Congr':  # 回應的文字若以 Congr 開頭就表示成功了
        print('已傳送 (' +str(v1)+', '+str(v2)+', '+str(v3)+ ') 到 Line')
    return r.text

ret = send_ifttt('台積電', 99, '建議買進')  #傳送 HTTP 請求到 IFTTT
print('IFTTT 的回應訊息：', ret)     # 輸出 IFTTT 回應的文字
