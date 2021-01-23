import numpy as np

array1 = np.array([[10, 8], [3, 5]])


# 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
invA1 = np.linalg.inv(array1)
orgA1 = np.matmul( array1, invA1)
print('observe if it is a identity matrix : %s' %orgA1)
# 運用上列array計算特徵值、特徵向量?
w, v = np.linalg.eig(array1)
print('eigenvalues  %s' % w)
print('eigenvectors %s' % v)

# 運用上列array計算SVD?
u, s, vh = np.linalg.svd(array1)
print('singular value decomposition: u  %s' % u)
print('singular value decomposition: s  %s' % s)
print('singular value decomposition: vh  %s' % vh)