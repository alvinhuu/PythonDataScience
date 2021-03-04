# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics

'''
# 離散均勻分配 (Discrete Uniform Distribution)
# 前提：其中有限個數值擁有相同的機率。
'''
# 1.定義離散均勻分配的基本資訊

low=1 
high=7
r = np.arange(low,high)
# 2.計算離散均勻分配的概率質量分佈 (probability mass function)
# 之所以稱為質量，是因為離散的點
# 產生 x 軸的點
#r = np.arange(stats.randint.ppf(0.01, low, high),
#              stats.randint.ppf(0.99, low, high),1)
print(r)
# P(X=x) --> 是機率
probs = stats.randint.pmf(r,low,high)
print(probs)
plt.bar(r, probs)
plt.ylabel('P(X=x)')
plt.xlabel('x')
plt.title('pmf of DU(1,6)')
plt.show()