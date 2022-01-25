import twstock

stock = twstock.Stock('2330')  # 以台積電的股票代號建立 Stock 物件
print(stock.price)             # 輸出最近 31 日的收盤價
