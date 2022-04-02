def moon_weight(now,weight_year):
    now = now*0.165
    weight_year = weight_year*0.165
    for year in range (1,15):
        print("Year%d Your weight On Moon is %d Kg"%(year,now+weight_year))
        now = now+weight_year

