# 參考網站 https://www.finlab.tw/%e8%b6%85%e7%b0%a1%e5%96%ae%e5%8f%b0%e8%82%a1%e6%af%8f%e6%97%a5%e7%88%ac%e8%9f%b2%e6%95%99%e5%ad%b8/

import requests
from io import StringIO
import pandas as pd
import numpy as np

datestr = '20200131'

# 下載股價
r = requests.post('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

# 整理資料，變成表格
df = pd.read_csv(StringIO(r.text.replace("=", "")), 
            header=["證券代號" in l for l in r.text.split("\n")].index(True)-1)

# 整理一些字串：
df = df.apply(lambda s: pd.to_numeric(s.astype(str).str.replace(",", "").replace("+", "1").replace("-", "-1"), errors='coerce'))

# 顯示出來
df.head()