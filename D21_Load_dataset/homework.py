# 導入必要的程式庫
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得鳶尾花資料集
# df = sns.load_dataset('iris')
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
# 取得資料集
df = sns.load_dataset('titanic')
df.info()
# 做箱形圖
sns.barplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()
# 在上面的示例中,我們可以看到每個class中男性和女性的平均存活率。從情節中,我們可以理解,女性存活人數比男性多。在男性和女性中,更多的存活率來自頭等艙。

# 利用 FacetGrid 繪圖並分析
# 瞭解性別在各艙等的分布的存活率, 用 survived 跟 sex 拆開
g = sns.FacetGrid(df, col = "survived")
g.map(plt.hist,"sex")
plt.show()
#先檢視各艙位存活人數，此時可以使用groupby函數進行分類，
#其中 survived＝1表示存活，survived＝0表示死亡，將survived加總即為各艙等生存人數。
df.groupby('pclass').survived.sum()
#加上性別
survived=df.groupby(['pclass','sex']).survived.sum()
survived.plot(kind='bar')
#使用pd.crosstab函數繪製交叉表，交叉表可以很直觀的依據艙位等級及性別來查看存活人數及死亡人數。
#繪製堆疊條形圖，x軸代表依據艙等分成男性及女性，y軸代表人數，其中藍色代表死亡人數，橘色代表存活人數。
survived_counts = pd.crosstab([df.pclass, df.sex],df.survived)
print( survived_counts )
survived_counts.plot(kind='bar', stacked=True)
plt.show()
# 繪製小提琴圖 
# 直接使用PANDAS dataframe, 當作參數
#條形圖()顯示分類變數和連續變數之間的關係。數據以矩形條表示,其中條的長度表示該類別中數據的比例。
sns.violinplot(data=survived_counts)
plt.show()
# 瞭解性別在各艙等的分布的存活率 
g = sns.FacetGrid(df, col = "survived")
g.map(plt.hist,"pclass")
plt.show()

# 可以嘗試其他的參數對照組合

# 0 survived
# 1 pclass
# 2 sex
# 3 age
# 5 parch
# 6 fare
# 7 embarked
# 8 class
# 9 who
# 10 adult_male
# 11 deck
# 12 embark_town
# 13 alive
# 14 alone