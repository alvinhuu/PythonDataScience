import pandas as pd  
import numpy as np
import urllib3
# from bs4 import BeautifulSoup
import yfinance as yf
import matplotlib.pyplot as plt
import time
import os
import seaborn as sns
from matplotlib import pyplot as plt

# timestr = time.strftime("%Y%m%d-%H%M%S")
timestr = time.strftime("%Y%m%d")

# 參考網站
# https://medium.com/ai%E8%82%A1%E4%BB%94/%E7%94%A8-python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E5%BA%AB-%E7%BE%8E%E8%82%A1%E7%AF%87-e3e896659fd6

# https://medium.com/ai%E8%82%A1%E4%BB%94/%E7%94%A8-python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E5%BA%AB-%E7%BE%8E%E8%82%A1%E7%AF%87-e3e896659fd6
# 最近一日交易量最大的前 100 檔熱門美股
url = 'https://finance.yahoo.com/screener/predefined/most_actives?count=200&offset=0'
data = pd.read_html(url, flavor="bs4")[0]
data.columns = ['symbol','name','price','changePrice','changePercent','vol','avgVol','MarketCap','TTM','52wkRange']
# a = sorted(a, key=lambda a_entry: a_entry[1]) 
# data1 = data[np.argsort(data[::, 0])]

def p2f(x):
    if not x.isdigit():
        return float(x.strip('%'))/100
    return x


def Money2int(x):
    m = {'K': 3, 'M': 6, 'B': 9, 'T': 12}
    if x.isdigit():
        return float(x)
    return (float(x[:-1]) * 10 ** m[x[-1]] )

def over3(x):
    A = Money2int(x[5])
    B = Money2int(x[6])
    P = p2f(x[4])
    L = ( A>B and P>=0.03 )
    return L

def sort3to10(x):
    A = Money2int(x[5])
    B = Money2int(x[6])
    P = p2f(x[4])
    L = ( A>B and ( P>=0.03 and P<= 0.1))
    return L

def big10(x):
    A = Money2int(x[5])
    B = Money2int(x[6])
    P = p2f(x[4])
    L = ( A>B and P > 0.1)
    return L

def setFunc( func ):
    newlist =  list( filter(func, data.values) )
    if newlist:
        d = np.row_stack(newlist)
        return pd.DataFrame({'Symbol': d[:, 0], 'Name': d[:, 1], 'price': d[:, 2], 'Change': d[:, 3], 'Change%': d[:, 4], 'MarketCap': d[:, 7], 'Vol': d[:, 5], 'avgVol(3m)': d[:, 6] }).sort_values(by=['Change%','MarketCap','Vol'], ascending=False)
    else:
        return 'None in list'

# dataframe = pd.DataFrame.from_records(d)
# dataset.boxplot()
print(setFunc(big10))
print(setFunc(sort3to10))

if 0:
    Over3 = setFunc(over3)
    print(timestr)
    path = r".\Most_Active_Over3.xlsx"
    if os.path.isfile(path) and os.access(path, os.R_OK):
        print("File exists and is readable")
        with pd.ExcelWriter(path, engine='openpyxl', mode='a') as writer:    
            Over3.to_excel( writer , sheet_name='A'+timestr)
    else:
        print("Either the file is missing or not readable")
        with pd.ExcelWriter(path) as writer:    
            Over3.to_excel( writer , sheet_name='A'+timestr)


