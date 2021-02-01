import pandas as pd  
import numpy as np
import urllib3
# from bs4 import BeautifulSoup
import yfinance as yf
import matplotlib.pyplot as plt

# 參考網站
# Yahoo! module
#https://pypi.org/project/yfinance/
# Get the data of the stock AAPL 
data = yf.download('QS','2020-01-01','2021-01-01') 
print(data) 
# # Plot the close price of the AAPL 
# data.Close.plot() 
# plt.show() 