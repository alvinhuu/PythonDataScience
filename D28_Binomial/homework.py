import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics


# 今天學到五種分配，包含，
# 離散均勻分配( Discrete Uniform Distribution )
# 伯努利分配( Bernoulli Distribution )
# 二項分配(Binomial Distribution)
# 負二項分配(Negative Binomial Distribution)
# 超幾何分配(Hypergeometric Distribution)
# 今天我們透過作業中的問題，回想今天的內容吧!

# Q1: 大樂透的頭獎，你必須從49個挑選出 6 個號碼，
# 且這六個號碼與頭獎的六個號碼一致，頭獎的機率是屬於哪一種分配?
# library

print('''Q1: 大樂透的頭獎，你必須從49個挑選出 6 個號碼，
可以想像成，大樂透中有49個號碼，6個是屬於開獎抽出的數字那一群，43個是不屬於開獎抽出的數字那一群，  
那你挑的六組號碼，有多少個是落在開獎抽出的數字那一群?
 屬於 超幾何分配.
''')
# Q2: 運用範例的 python 程式碼，計算大樂透的中頭獎機率?
probs = stats.hypergeom.pmf(6,49,6,6)
print("中頭獎的機率為==",probs)
#Q3: 你覺得電腦簽注的中獎機率，和人腦簽注相比，哪一個機率高?
print('以機率的角度來看，兩者一樣高')
