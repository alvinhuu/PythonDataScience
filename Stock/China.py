import pandas as pd  
import numpy as np
import urllib3
# from bs4 import BeautifulSoup
import yfinance as yf
import matplotlib.pyplot as plt
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

# 參考網站
# https://www.cnyes.com/usastock/adrprice.aspx?t=area&v=cn

url = 'https://www.cnyes.com/usastock/adrprice.aspx?t=area&v=cn'
data = pd.read_html(url, flavor="bs4")[0]
data.columns = ['時間','代碼','名稱','成交','漲跌','漲%','開盤','最高','最低','成交量','上市日期','IPO價格']
# a = sorted(a, key=lambda a_entry: a_entry[1]) 
# data1 = data[np.argsort(data[::, 0])]
# print(data)

def p2f(x):
    if not x.isdigit():
        return float(x.strip('%'))/100
    return x

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
        return pd.DataFrame({'Symbol': d[:, 0], 'Name': d[:, 1], 'price': d[:, 2], 'Change': d[:, 3], 'Change%': d[:, 4], 'Vol': d[:, 8], 'avgVol(3m)': d[:, 6] })
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
