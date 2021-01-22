import numpy as np

array1 = np.array(range(30))
array2 = np.array([2,3,5])
array3 = np.array([[4,5,6], [1,2,3]])
#將兩列 array 存成 npz 檔
with open('array.npz','wb') as f:
    np.savez(f, array1, array2) 

#讀取剛剛的 npz 檔，加入下列 array 一起存成新的 npz 檔
npzfile = np.load('array.npz')
A1 = npzfile['arr_0']
A2 = npzfile['arr_1']

print(A1, A2)

with open('final123.npz','wb') as f:
    np.savez(f, A1, A2, array3)

Finally=np.load('final123.npz')
print(Finally.files)