import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# 比較好的教學 https://zhuanlan.zhihu.com/p/27816821

# 作業目標(1)：
# 繪製模型殘差 圖型


#設定圖形樣式 - whitegrid
# sns.set_style('whitegrid')
sns.set(style='whitegrid')

# 利用 NUMPY 去建立資料集 
rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75) 
# 畫圖
sns.residplot(x=x, y=y, lowess=True, color="g")

plt.show()
# 作業目標(2)：
# 使用 distplot()使用簡單的規則來正確猜測預設情況下正確的數位,但嘗試更多或更少的 bin 可能會顯示資料中的其他特徵：
# 有無kde對圖形分布的影響
# bin: 指的是特徵值, 
sns.set(color_codes=True)

# bin: 指的是特徵值, 
# kde: on/off
sns.distplot(x=x, bins=15, kde=False, rug=True);
plt.show()
###
sns.distplot(x=x, bins=15, kde=True, rug=True);
plt.show()
