from numpy.random import normal,uniform
from numpy.random import seed
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
import math
import pylab
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')
# %matplotlib inline

## Q1:計算標準常態分配，小於1的機率有多大?
## 常態分配的計算
# 計算標準常態分配記Ｘ　介於 1,-1的比例
mu=0
sigma=1
b=  stats.norm.cdf(1,mu, sigma)
print("P(Z<1)=",b)

## Q2:計算標準常態分配，大於1，小於 -1 的機率有多大?
## 先算 p(<-1X<1)，再算  P(X>1 or X<-1)
mu=0
sigma=1
b=  stats.norm.cdf(1,mu, sigma)
a=  stats.norm.cdf(-1,mu, sigma)
print("P(Z>1 or Z<-1)=",1-(b-a))

## Q3: X~N(2,4),x 服從常態分配，平均數為2,變異數為 4，計算 X小於 6 的機率有多大?
#算法1
mu=0
sigma=1
b=  stats.norm.cdf(2,mu, sigma)
print("P(Z<2)=",b)

#算法2
mu=2
sigma=2 #( 4 要開根號)
b= stats.norm.cdf(6,mu, sigma)
print("P(X<6)=",b)