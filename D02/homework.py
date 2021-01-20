import numpy as np

array1 = np.array(range(30))
a = array1.reshape((5,6), order='F')
print(a)
b = np.where(a%6==1,a," ")
c = np.where(a%6==1)
print(b)
print(c)