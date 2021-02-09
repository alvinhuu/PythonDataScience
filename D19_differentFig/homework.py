import pandas as pd  
import matplotlib.pyplot as plt  #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html
import numpy as np

# 條型圖：Bar Plots

# 長條圖主要用來呈現兩個維度的資料，一個為X軸另一個則為Y軸(當然這邊指的是二維的狀況，較為常見)
# 主要用來呈現兩個維度的資料
# 問題：嘗試通過添加紅色條形標籤重現右側的圖形。
plt.axes([0.1,0.1,.5,.5], facecolor='red')
# Set locations and labels
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)
plt.show()

# 軸圖進階

# 但是可以將圖放置在圖中的任何位置。因此，如果要在較大的圖中放置較小的圖，則可以使用軸。
# 特別提醒：tick 刻度線定位器
# 問題：使用 tick


 #配置12 組 Bar
n = 12 
X = np.arange(n)

 #給定數學運算式
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

#指定上半部繪製區域, 給定 Bar 顏色, 邊界顏色, https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html
plt.bar(X, +Y1, facecolor='red', edgecolor='white')
# +Y 指的是 XY 四象限的第一象限
plt.bar(X, -Y2, facecolor='#1111ff', edgecolor='white')


 #設定繪圖圖示區間
for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

 #設定Y軸區間
plt.ylim(-1.25,+1.25)
plt.show()