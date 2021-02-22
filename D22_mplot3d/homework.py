import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# install tensorflow and keras
# https://medium.com/@virginiakm1988/%E5%9C%A8-anaconda-%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83%E4%B8%8B%E5%AE%89%E8%A3%9D-tensorflow%E8%88%87-keras-c2c5aed98fef
# 需要使用 Colab 請注意一下
# 先行確認 Colab 上面的版本
import keras
print("keras:",keras.__version__)
import tensorflow as tf
print("tf:",tf.__version__)
# 需要使用 Colab 請注意一下
# Training code
# 新增網路硬碟
from google.colab import drive
drive.mount("/gdrive", force_remount=True)
#drive.mount('/gdrive')
 

# # 瞭解有關資料集屬性
# # 我們可以使用 info()或是 descript() 方法瞭解有關資料集屬性的更多資訊。特別是行和列的數量、列名稱、它們的數據類型和空值數。
#     # 記錄數、平均值、標準差、最小值和最大值，我們使用 describe()
# df. describe()
#     # 瞭解有關資料集屬性的更多資訊。特別是行和列的數量、列名稱、它們的數據類型和空值數。
# df.info()
#     # 處理缺失值
# df = pd.get_dummies
# 資料集的處理
# 有時候無法從資料集明確的看出資料的屬性與因子的相互關係，要針對資料做處理

# https://kknews.cc/code/lnnxmr9.html

