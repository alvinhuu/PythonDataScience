# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics

# 離散均勻分配( Discrete Uniform Distribution )
# 伯努利分配( Bernoulli Distribution )
# 二項分配(Binomial Distribution)
# 今天我們透過作業中的問題，回想今天的內容吧!
# 丟一個銅板，丟了100次，出現正面 50 次的機率有多大。

'''
你的答案 
'''
# 這是 bermoulli分配
p = 0.5 # 假設是公平硬幣
n = 100  # 重複實驗 100次,
r = 50 # 計算出現50次正面


# 2.計算二項分佈的概率質量分佈 (probability mass function)
# 之所以稱為質量，是因為離散的點
# P(X=x) --> 是機率
probs = stats.binom.pmf(r, n, p)
print(probs)