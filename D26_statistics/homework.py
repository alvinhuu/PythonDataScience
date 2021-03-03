# 今天學到不同統計量之間特性，
# 試著分析男生女生身高資料，
# 試著回答下面的問題:
# Q1:試著用今天所教的內容，如何描述這兩組資料的樣態?
# Q2: 請問男生和女生在平均身高上誰比較高?
# Q3:請問第二題的答案和日常生活中觀察的一致嗎? 如果不一致，你覺得原因可能為何?
# 上述問題透過 python 語法進行運算， 並將上述答案填寫在 (google 表單)[https://docs.google.com/forms/d/e/1FAIpQLSdDzwpeJl8YLPwZaW8pBZvtuXY9kIbbZLqxcXyzFaoraV5JEA/viewform ] 

# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns

#輸入資料
boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170, 164, 173, 165, 163, 177, 171]
print(sorted(boys))
# 計算統計量_平均數的方法
mean_boy=np.mean(boys)
print("男孩身高平均=",mean_boy)

statistics_mean_boy=statistics.mean(boys)
print("statistics_mean_boy=",statistics_mean_boy)
 

# 計算統計量_中位數的方法
np_median_boy=np.median(boys,axis=None)
print("np_median_boy=",np_median_boy) 

statistics_median_boy=statistics.median(boys)
print("statistics_median_boy=",statistics_median_boy)

# 統計量_眾數
# 統計量的眾數，如果有多個眾數，取最小的值當眾數。

mode_boy=stats.mode(boys,axis=None)
print("男孩身高眾數=",mode_boy)
print("男孩身高眾數=",mode_boy[0][0])

# 統計量_眾數
statistics_mode_boy=statistics.mode(boys)
print("statistics_mode_boy=",statistics_mode_boy)

#全距
#rangeV=max(boys)-min(boys)
def rangeV(x): 
  return(max(x)-min(x))
    
print(rangeV(boys))

# 計算變異數的方法
print("男孩身高變異數=",statistics.variance(boys))
print("男孩身高變異數=",np.var(boys,ddof=1))

# 統計量_標準差的方法
#樣本標準差
#ddof=1, 回傳 sample standard deviation 樣本標準差，分母(n-1)，無偏估計
std_boy=np.std(boys,ddof=1)
print("男孩身高標準差=",std_boy)

statistics_stdev_boy=statistics.stdev(boys)
print("statistics_mean_boy=",statistics_stdev_boy)

# python 百分位數
#np
print("90百分位數=",np.percentile(boys, 90))
print("50百分位數=",np.percentile(boys, 50))
print("20百分位數=",np.percentile(boys, 20))
#stat
print("20百分位數=",stats.scoreatpercentile(boys, 20))

#計算峰度和偏度
print(stats.skew(boys))
print(stats.kurtosis(boys))

# pandas和 stat 接近
# python的峰帶

#最後，畫圖看分布
plt.hist(boys,alpha=.4,bins=40)
plt.title('boy,skewness={0},kurtosis={1}'.format(round(stats.skew(boys),2),round(stats.kurtosis(boys),2)))
plt.axvline(x=mean_boy)
plt.show()
