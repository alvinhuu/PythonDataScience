import numpy as np

# https://numpy.org/doc/stable/reference/arrays.dtypes.html
# '?'  boolean
# 'b'  (signed) byte
# 'B'  unsigned byte
# 'i'  (signed) integer
# 'u'  unsigned integer
# 'f'  floating-point
# 'c'  complex-floating point
# 'm'  timedelta
# 'M'  datetime
# 'O'  (Python) objects
# 'S', 'a'  zero-terminated bytes (not recommended)
# 'U'  Unicode string
# 'V'  raw data (void)

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

# 將上列 list 依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入 array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
# dt=np.dtype('U, U, f, i, ?')
# dt=np.dtype({'names':(),'formats':()})
dt=np.dtype({'names':('name', 'sex', 'weight', 'rank', 'myopia'),'formats':('U5', 'U5', 'f', 'i', '?')})
a=np.zeros(8,dtype=dt)
a['name']=name_list
a['sex']=sex_list
a['weight']=weight_list
a['rank']=rank_list
a['myopia']=myopia_list
print(a)

# 呈上題，將 array 中體重(weight)數據集取出算出全部平均體重
b=np.average(a['weight'])
print('全部平均體重 %f' % b)

# 呈上題，進一步算出男生(sex 欄位是 boy)平均體重、女生(sex 欄位是 girl)平均體重
a_where = np.where(a['sex']=='boy')
# print(a_where)
avBoy=np.average( a[a_where]['weight'] )
print('男生(sex 欄位是 boy)平均體重 %f' % avBoy)
b_where = np.where(a['sex']=='girl')
# print(b_where)
avGirl=np.average( a[b_where]['weight'] )
print('女生(sex 欄位是 girl)平均體重 %f' % avGirl)