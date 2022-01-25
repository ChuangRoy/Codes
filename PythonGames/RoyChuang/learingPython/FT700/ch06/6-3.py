import twstock

stock = twstock.Stock('2330')    # 以台積電的股票代號建立 Stock 物件
print(stock.moving_average(stock.price, 5))  # 計算五日平均價格

