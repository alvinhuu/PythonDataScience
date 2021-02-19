# 導入必要的程式庫
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得鳶尾花資料集
df = sns.load_dataset('iris')
# 箱形圖顯示了數據的總體分布，同時繪製了異常值的數據點。這個物理點讓它們的特定值在樣本之間容易被識別和比較。
# sns.boxplot(data = df, orient = "h")
# 當一個或兩個正在研究的變數是分類的時，我們使用像條帶線()、swarmplot()等的圖。
# 查看到每個物種petal_length的差異。但是，散點圖的主要問題是散點圖上的點重疊。
# sns.stripplot(x = "species", y = "petal_length", data = df)
# 上述散點圖的主要問題是散點圖上的點重疊。我們使用"抖動"參數來處理此類方案。
# 抖動會為數據添加一些隨機雜訊。此參數將沿分類軸調整位置。
# sns.stripplot(x = "species", y = "petal_length", data = df, jitter=True)
# 另一個可以用作「抖動」 的替代選項是函數群圖(), 此函數將散點圖的每個點都放在分類軸上，從而避免重疊點
# sns.swarmplot(x = "species", y = "petal_length", data = df)

# 核密度估計(Kernel Density Estimates, KDE)
# 可以觀察每個情節的變化。繪圖採用矩陣格式，其中行名表示 x 軸，列名稱表示 y 軸。
# 對角線圖是內核密度圖，其中其他圖是散點圖
# 內核密度估計是估計變數分佈的非參數化方法。
# sns.set_style("ticks")
# sns.pairplot(df,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
# 可以在上三角形和下三角形使用不同的函數來查看關係的不同方面
# g = sns.pairplot(df,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot, cmap = "Blues_d")
# g.map_diag(sns.kdeplot, lw = 3, legend = False)

# plt.show()

# FacetGrid 類有助於可視化一個變數的分佈，以及使用多個面板在數據集子集中分別顯示多個變數之間的關係
# 作業：取得另一個 dataset：titanic
df.info()
# 做箱形圖
sns.boxplot(data = df, orient = "h")
# 利用 FacetGrid 繪圖並分析
g = sns.FacetGrid(data = df, col='species',hue = 'species')
g.map(plt.plot, 'X', 'Y1')
plt.show()
# 繪製小提琴圖 
sns.violinplot(x="day", y="total_bill", hue="smoker", data=df, palette="muted",split=True)
plt.show()