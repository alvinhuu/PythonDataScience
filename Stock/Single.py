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
print( yf.download('TLRY','2020-12-01','2021-03-01') )
print( yf.download('APHA','2020-12-01','2021-03-01') )
# # Plot the close price of the AAPL 
# data.Close.plot() 
# plt.show() 