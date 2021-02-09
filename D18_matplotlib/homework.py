import pandas as pd  
import matplotlib.pyplot as plt
import numpy as np

# 1.   畫出 cos 圖檔，並儲存
# x = np.arange(0,360)
# y = np.cos(x*np.pi/180.0)
# plt.plot(x,y, color = 'red')

#Correction
#畫出完整的 cos 圖形
x = np.arange(0, 3 * np.pi, 0.1)
y = np.cos(x)
# or
x = np.arange(0,180)
y = np.cos(2*x*np.pi/180.0)
#角度轉弧度
x = np.deg2rad(x)

plt.plot(x, y)

 # 照需要寫入x 軸和y軸的 label 以及title	
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("Cos graphic") 
plt.savefig("cos.png",dpi=300,format="png")
plt.show()

# 2.    給定散點圖顏色
n=1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
plt.title("Scatter plot")
plt.scatter(X, Y, color = 'gold')
#correction
#這邊是做三角函數的運算，把資料分成四個值, 用arc tangent把Y X 轉換成0~1的浮點數,剛好這些浮點數會對應到scatter裡面的色碼錶
T = np.arctan2(Y,X)
#https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.scatter.html
#alpha:  範圍從 0 - 1，數字越大代表越透明
plt.scatter(X,Y, s=75, c=T, alpha=.5)   
#設定各個軸的極限
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

# 如果要存成圖形檔: 
# 把 pyplot.show() 換成下面這行:
plt.savefig("Scatter.png",dpi=300,format="png")
plt.show()
