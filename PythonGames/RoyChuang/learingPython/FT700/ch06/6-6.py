import twstock

def get_price(stockid):   # 取得股票名稱和及時股價
    rt = twstock.realtime.get(stockid)   # 取得台積電的及時交易資訊
    if rt['success']:                    # 如果讀取成功
        return (rt['info']['name'],      #←傳回 (股票名稱, 及時價格)
                float(rt['realtime']['latest_trade_price']))
    else:
        return (False, False)

def get_best(stockid):     # 檢查是否符合四大買賣點
    stock = twstock.Stock(stockid)
    bp = twstock.BestFourPoint(stock).best_four_point()
    if(bp):
        return ('買進' if bp[0] else '賣出', bp[1])  #←傳回買進或賣出的建議
    else:
        return (False, False)  #←都不符合

name, price = get_price('2330')  #←用 name 及 price 來承接傳回的 tuple
act, why = get_best('2330')      #←用 act 及 why 來承接傳回的四大買賣點 tuple
print(name, price, act, why, sep=' | ')
