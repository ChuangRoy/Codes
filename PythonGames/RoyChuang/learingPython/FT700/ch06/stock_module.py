def get_setting():   # 取得 stock.txt 中的股票設定資訊
    try:
        with open('stock.txt') as f:  #←以讀取模式開啟檔案
            slist = f.readlines()     #←以行為單位讀取所有資料
#            print('讀入：', slist)
            res = []
            for lst in slist:
                s = lst.split(',')
                res.append([s[0], float(s[1]), float(s[2])])
    except:
        print('stock.txt 讀取錯誤')
        return None
    return res


import twstock

def get_price(stockid):   # 取得股票名稱和及時股價
    rt = twstock.realtime.get(stockid)   # 取得台積電的及時交易資訊
    if rt['success']:                    # 如果讀取成功
        return (rt['info']['name'],      #←傳回 (股票名稱, 及時價格)
                float(rt['realtime']['latest_trade_price']))
    else:
        return (False, False)

def get_best(stockid):    # 檢查是否符合四大買賣點
    stock = twstock.Stock(stockid)
    bp = twstock.BestFourPoint(stock).best_four_point()
    if(bp):
        return ('買進' if bp[0] else '賣出', bp[1])  #←傳回買進或賣出的建議
    else:
        return (False, False)  #←都不符合


import requests      # 匯入 requests 套件

def send_ifttt(v1, v2, v3):   # 送出包含 3 個網址參數的 HTTP GET 要求
    url = ('https://maker.ifttt.com/trigger/toline/with/' +
          'key/ckyTQ8zoYfDiJgha830XbL' +
          '?value1='+str(v1) +
          '&value2='+str(v2) +
          '&value3='+str(v3))
    r = requests.get(url)      # 送出 HTTP GET
    if r.text[:5] == 'Congr':  # 傳回文字若以 Congr 開頭就表示成功了
        print('已傳送 (' +str(v1)+', '+str(v2)+', '+str(v3)+ ') 到 Line')
    return r.text