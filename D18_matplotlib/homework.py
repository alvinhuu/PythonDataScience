import pandas as pd  
import matplotlib.pyplot as plt
import numpy as np

# 1.   畫出 cos 圖檔，並儲存
x = np.arange(0,360)
y = np.cos(x*np.pi/180.0)
plt.plot(x,y, color = 'red')

 # 照需要寫入x 軸和y軸的 label 以及title	
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("Cos graphic") 
plt.savefig("cos.png",dpi=300,format="png")
plt.show()

# 2.    給定散點圖顏色
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
plt.scatter(X, Y, color = 'gold')
plt.title("Scatter plot")

# 如果要存成圖形檔:
# 把 pyplot.show() 換成下面這行:
plt.savefig("Scatter.png",dpi=300,format="png")
plt.show()
