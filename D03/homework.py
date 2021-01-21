import numpy as np

V1 = 20000
V0 = 20

def db2V1(db):
    return np.power(10,db/20)*V0

gdb = 20*np.log10(V1/V0)
print('正常的談話的聲壓為 20000 微巴斯卡，請問多少分貝: answer is %d db' % gdb)

V30db = db2V1(30)
V50db = db2V1(50)

print('30db\'s V1 is %d' % V30db)
print('50db\'s V1 is %d' % V50db)

print('30 分貝的聲壓會是 50 分貝的幾倍 = {:.3f}'.format(V30db/V50db) )

