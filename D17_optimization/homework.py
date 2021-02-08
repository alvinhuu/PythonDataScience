import pandas as pd  
import numpy as np


# 有三個方法帶給大家，可以大幅減少程式的執行時間

# 讀取資料型態選最快速的 | 之後如果遇到讀取資料慢時，不妨使用 pkl 檔讀取看看。 (Don't use csv)
# 多使用內建函數 |  groupby+agg+ 內建函數是最快的, 如果非得需要用到自己的函式，那盡量使用 agg 會比 transform 來的快速
# 向量化的資料處理 | 採用 isin() 篩選出對應資料室最快的，速度快是因為它採用了向量化的資料處理方式（這裡的 isin() 是其中一種方式，還有其他方式


# 資料型態非常多種，在大數據的情況第一關往往都是資料讀取，以下四種資料型態進行實測，可以發現讀取速度以 pkl 檔為最快，是平常讀 csv 的 6 倍速，
# 當然不同環境與不同資料會有所差距，不過資料越多改善會越明顯。

# 題目 : 

# 在速度較慢的時候，可以先從哪邊開始檢查？
print('在速度較慢的時候，可以先從是否使用內建函數開始檢查')
# 資料過大時應採取什麼方式讓記憶體占用量下降？
print('資料過大時應採取: \n1.將欄位的型態降級，不需要存太多元素在一個數字中')
print('2. 將整數型態 int 改成 uint 減少記憶體正用空間 int_data.apply(pd.to_numeric,downcast=unsigned')
print('3. 將浮點數型態 float64 改成 float32 減少記憶體正用空間 float_data.apply(pd.to_numeric,downcast=float')