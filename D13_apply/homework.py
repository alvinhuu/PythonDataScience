import pandas as pd  
import numpy as np
# 對以下成績資料做分析

score_df = pd.DataFrame([[1,56,66,70], [2,90,45,34], [3,45,32,55], [4,70,77,89], [5,56,80,70], [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
print(score_df)

# 6 號學生(student_id=6) 3 科平均分數為何？
noCol0 = np.delete(score_df.values,0,axis=1)
# print('6 號學生(student_id=6) 3 科平均分數 %s' % noCol0.mean(axis=1)[5])
df=score_df.drop(columns='student_id',axis=1)
print('6 號學生(student_id=6) 3 科平均分數 %s' % df.values.mean(axis=1)[5])
# 6 號學生 3 科平均分數是否有贏過班上一半的同學？
print('中位數 %s' % df.mean(axis=1).median())
if noCol0.mean(axis=1)[5] > df.mean(axis=1).median() :
    print('Yes, 6 號學生 3 科平均分數有贏過班上一半的同學')
else:
    print('No, 6 號學生 3 科平均分數沒有贏過班上一半的同學')
# 由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？
newscore = df.apply(lambda x : x**(0.5)*10)
print('加分後 6 號同學 3 科成績分別是')
print(list(newscore.columns) )
print(newscore.values[5])

# 承上題，加分後各科班平均變多少
print('加分後各科班平均變多少 \n%s' % newscore.mean())

# 範例程式臨摹
print('--------------------------')
Exdf = pd.DataFrame([[1,56,66,70], [2,90,45,34], [3,45,32,55], [4,70,77,89], [5,56,80,70], [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
Exdf = Exdf.set_index('student_id')

print(Exdf.mean(axis=1)[6])
print(Exdf.mean(axis=1).median())
print(Exdf.apply(lambda x: x**(0.5)*10))
print(Exdf.apply(lambda x: x**(0.5)*10).values[5])  #values uses old index rule