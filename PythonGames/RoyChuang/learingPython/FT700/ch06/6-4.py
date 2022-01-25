import twstock

stock = twstock.Stock('2330')      # 建立台積電的 Stock 物件
bfp = twstock.BestFourPoint(stock) # 以 stock 建立四大買賣點物件
print(bfp.best_four_point())       # 判斷是否為四大買賣點