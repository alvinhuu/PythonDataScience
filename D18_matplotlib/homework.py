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
y_cos = np.cos(x)
plt.plot(x, y_cos)

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
T = np.arctan2(Y,X)
plt.scatter(X,Y, s=75, c=T, alpha=.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

# 如果要存成圖形檔:
# 把 pyplot.show() 換成下面這行:
plt.savefig("Scatter.png",dpi=300,format="png")
plt.show()
