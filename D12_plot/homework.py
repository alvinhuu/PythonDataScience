import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt


# 題目 : 將資料夾中 boston.csv 讀進來，並用圖表分析欄位。
bd = pd.read_csv('boston.csv') 
df = pd.DataFrame(bd) 
# 畫出箱型圖，並判斷哪個欄位的中位數在 300~400 之間？
df.boxplot()
print('TAX and B 的中位數在 300~400 之間')
# 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？
df.plot.scatter(x='NOX', y='DIS')
plt.show()
print('當NOX數值較低的時候, DIS 數值較高, 反之, 當NOX數值較高的時候, DIS 數值較低 ')

