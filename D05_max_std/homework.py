import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

#上 3 列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文 55 分 
# 、數學 60 分、國文 65 分，今天第五位同學因某原因沒來考試，導致數學成績缺值
def Tavg():
    EngAvg = np.average(english_score)
    MathAvg = np.nanmean(math_score)
    ChtAvg = np.average(chinese_score)
    print('各科成績平均 %s' % EngAvg,MathAvg,ChtAvg)

def Tmax():
    EngMax = np.nanmax(english_score)
    MathMax = np.nanmax(math_score)
    ChtMax = np.nanmax(chinese_score)
    print('各科成績最大值 %s' %EngMax,MathMax, ChtMax)

def Tmin():
    EngMin = np.nanmin(english_score)
    MathMin = np.nanmin(math_score)
    ChtMin = np.nanmin(chinese_score)
    print('各科成績最小值 %s' %EngMin,MathMin, ChtMin)

def Tstd():
    EngStd = np.nanstd(english_score)
    MathStd = np.nanstd(math_score)
    ChtStd = np.nanstd(chinese_score)
    print('各科成績標準差 %s' %EngStd,MathStd, ChtStd)

print("             English    Math    Chinese")
#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略？
Tavg()
Tmax()
Tmin()
Tstd()

#2. 第五位同學補考數學後成績為 55，請計算補考後數學成績平均、最大值、最小值、標準差？
math_score[4]=55
print("補考數學後")
print("數學分數 ","平均",np.nanmean(math_score),"最大值",np.nanmax(math_score),"最小值",np.nanmin(math_score),"標準差",np.nanstd(math_score))

#3. 用補考後資料找出與國文成績相關係數最高的學科？
E=np.corrcoef(english_score, chinese_score)
M=np.corrcoef(math_score, chinese_score)
if np.maximum(E,M).all() :
    print("與國文成績相關係數最高的學科 is English")
else:
    print("與國文成績相關係數最高的學科 is Math")