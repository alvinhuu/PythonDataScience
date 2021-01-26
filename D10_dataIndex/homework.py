import pandas as pd

# 讀取 STOCK_DAY_0050_202009.csv 串聯 STOCK_DAY_0050_202010.csv，並且找出 open 小於 close 的資料

stock09 = pd.read_csv('STOCK_DAY_0050_202009.csv' )
stock10 = pd.read_csv("STOCK_DAY_0050_202010.csv" )
#串聯
stockFin = stock09.append(stock10)
# 答案的串聯
#stockFin = pd.concat([stock09,stock10])
# print(stock09[stock09.open<stock09.close])
# print(stock10[stock10.open<stock10.close])
print(stockFin[stockFin.open<stockFin.close])
