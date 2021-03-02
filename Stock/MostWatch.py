import pandas as pd  
import numpy as np
import urllib3
# from bs4 import BeautifulSoup
import yfinance as yf
import matplotlib.pyplot as plt
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

# 參考網站
# https://medium.com/ai%E8%82%A1%E4%BB%94/%E7%94%A8-python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E5%BA%AB-%E7%BE%8E%E8%82%A1%E7%AF%87-e3e896659fd6

# https://medium.com/ai%E8%82%A1%E4%BB%94/%E7%94%A8-python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E5%BA%AB-%E7%BE%8E%E8%82%A1%E7%AF%87-e3e896659fd6
# 最近一日交易量最大的前 100 檔熱門美股
url = 'https://finance.yahoo.com/u/yahoo-finance/watchlists/most-watched/'
data = pd.read_html(url, flavor="bs4")[1]
data.columns = ['symbol','name','price','changePrice','changePercent','Time','vol','avgVol','MarketCap']
# a = sorted(a, key=lambda a_entry: a_entry[1]) 
# data1 = data[np.argsort(data[::, 0])]
# print(data)

def p2f(x):
    if x.isdigit():
        return float(x.strip('%'))/100
    return 0


def Money2int(x):
    m = {'k':3, 'K': 3, 'M': 6, 'B': 9, 'T': 12}
    if x.isdigit():
        return float(x)
    return (float(x[:-1]) * 10 ** m[x[-1]] )

def over3(x):
    A = Money2int(x[6])
    B = Money2int(x[7])
    P = p2f(x[4])
    L = ( A>B and P>=0.03 )
    return L

def sort3to10(x):
    A = Money2int(x[6])
    B = Money2int(x[7])
    P = p2f(x[4])
    L = ( A>B and ( P>=0.03 and P<= 0.1))
    return L

def big10(x):
    A = Money2int(x[6])
    B = Money2int(x[7])
    P = p2f(x[4])
    L = ( A>B and P > 0.1)
    return L

def setFunc( func ):
    newlist =  list( filter(func, data.values) )
    if newlist:
        d = np.row_stack(newlist)
        return pd.DataFrame({'Symbol': d[:, 0], 'Name': d[:, 1], 'price': d[:, 2], 'Change': d[:, 3], 'Change%': d[:, 4], 'TTM': d[:, 8], 'Vol': d[:, 5], 'avgVol(3m)': d[:, 6] })
    else:
        return 'None in list'

# dataframe = pd.DataFrame.from_records(d)
# dataset.boxplot()
print(setFunc(big10))
print(setFunc(sort3to10))


Over3 = setFunc(over3)
print(timestr)
# Over3.to_excel('over3.xlsx', sheet_name='A'+timestr)
# data=data[np.argsort(data[:,0])]
# stk_list = data.Symbol
