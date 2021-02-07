import pandas as pd  
import numpy as np

# 題目：運下列時間序列資料做運算
index = pd.date_range("1/1/2021", periods=20, freq='D')
series = pd.Series(range(20), index=index)
# print(f'index= {index}')
print(series)
# 將所有轉為周資料
print( series.resample('W',convention='start').asfreq('D') )
# 將周資料的值取平均
print( series.resample('W').mean() )