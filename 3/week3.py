# -*- coding: utf-8 -*-
#向量相加-Python
'''
C:\Python27\python.exe
'''

def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

#向量相加-NumPy
import numpy as np

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

#效率比较
from datetime import datetime

size = 1000

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print "The last 2 elements of the sum", c[-2:]
print "PythonSum elapsed time in microseconds", delta.microseconds

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print "The last 2 elements of the sum", c[-2:]
print "NumPySum elapsed time in microseconds", delta.microseconds

#numpy数组
a = np.arange(5)
a.dtype

a
a.shape

#创建多维数组
m = np.array([np.arange(2), np.arange(2)])
print (m)
print (m.shape)
print m.dtype

#array是一行一行生成的，np.array([row1,row2,...,rown])

m1 = [np.arange(3),np.arange(3)] #not a array,but a list!!!!
# np.array turn a list into an array
print(m1)
type(m2)
print(m1.shape) #no shape
print(m1.dtype) # no dtype

# turn a tupple into an array
m2 = (np.arange(3),np.arange(3))
print(m2)
type(m2)
m2 = np.array(m2)
print (m2)
print (m2.shape)
print m2.dtype

# 生成多维矩阵
m2.reshape(2,3)
m2.reshape(6,1)
m2.reshape(2,1,3)

# creat a special array
np.zeros(10)
np.zeros((3, 6)) #3行6列的零向量
np.empty((2, 3, 2))#一个3维向量，组*行*列
np.arange(15)

#选取数组元素
a = np.array([[1,2],[3,4]])

print "In: a"
print (a)

print "In: a[0,0]"
print (a[0,0])

print "In: a[0,1]"
print a[0,1]

print "In: a[1,0]"
print a[1,0]

print "In: a[1,1]"
print a[1,1]

#numpy数据类型
print "In: float64(42)"
print np.float64(42)

print "In: int8(42.0)"
print np.int8(42.0)

print "In: bool(42)"
print np.bool(42)

print np.bool(0)

print "In: bool(42.0)"
print np.bool(42.0)

print "In: float(True)"
print np.float(True)
print np.float(False)

print "In: arange(7, dtype=uint16)"
print np.arange(7, dtype=np.uint16)

print "In: arange(7, dtype=float64)"
print np.arange(7, dtype=np.float64)

print "In: int(42.0 + 1.j)"
try:
   print np.int(42.0 + 1.j)
except TypeError:
   print "TypeError"
#Type error

print "In: float(42.0 + 1.j)"
print float(42.0 + 1.j)
#Type error

# 数据类型转换
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr.dtype

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
arr.astype(np.int32)

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)


#数据类型对象
a = np.array([[1,2],[3,4]])

print a.dtype.byteorder

print a.dtype.itemsize

#字符编码
print np.arange(7, dtype='f') #f=float
print np.arange(7, dtype='D') #D=double

print np.dtype(float)

print np.dtype('f')
print np.dtype('d') #d=float64

print np.dtype('D') #double

print np.dtype('f8') #f8 = float64

print np.dtype('Float64')


#dtype类的属性
t = np.dtype('Float64')

print t.char

print t.type

print t.str

#创建自定义数据类型
t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
print t

print t['name']

itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)

print itemz[1]

#数组与标量的运算
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
arr * arr
arr - arr

1 / arr
arr ** 0.5

#一维数组的索引与切片
a = np.arange(9)

print a[3:7] #pick from 3 to 6

print a[:7:2] # pick from 0 to 7，interval= 2

print a[::-1] # pick from the 1st one to the last one,"-1" == interval = 1 & in reverse order
print a[::-2]

s = slice(3,7,2) # (3,5)
print a[s]

s = slice(None, None, -1)
print a[s]

#多维数组的切片与索引
b = np.arange(24).reshape(2,3,4)

print b.shape

print b

print b[0,0,0]

print b[:,0,0] #from the 1st group to the last group,pick the first(0*0) one individually

print b[0] # pick the first group
print b[0, :, :] # == b[0]
print b[0, ...] # == b[0]

print b[0,1]
print b[0,1,::2]# first group, row 1, from 1st one  to 2nd one with inteval = 2

print b[...,1] # all group,all row, col 1

print b[:,1] #all group, row 1

print b[0,:,1] #1st group, all row, col 1

print b[0,:,-1]
 
print b[0,::-1, -1]


print b[0,::2,-1]

print b[::-1]

s = slice(None, None, -1)
print b[(s, s, s)]

#布尔型索引
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
names
data

names == 'Bob'
data[names == 'Bob']

data[names == 'Bob', 2:]
data[names == 'Bob', 3]

names != 'Bob'
data[names != 'Bob']


mask = (names == 'Bob') | (names == 'Will')
mask
data[mask]

data[data < 0] = 0
data

data[names != 'Joe'] = 7
data

#花式索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

arr

arr[[4, 3, 0, 6]]

arr[[-3, -5, -7]] #3,5,7 in reverse order

arr = np.arange(32).reshape((8, 4))
arr
arr[[1, 5, 7, 2], [0, 3, 1, 2]] #[1,0],[5,3]

arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]] # row[1,5,7,2],all col[0,3,1,2]

arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]

#数组转置
arr = np.arange(15).reshape((3, 5))
arr
arr.T

#改变数组的维度
b = np.arange(24).reshape(2,3,4)

print b

print b.ravel() # 向量化

print b.flatten()

b.shape = (6,4)

print b

print b.transpose()

b.resize((2,12))

print b

c = b.reshape(2,12)
d = b.resize(2,12)
c == d #False

#组合数组
a = np.arange(9).reshape(3,3)
print (a)

b = 2 * a

print b

print np.hstack((a, b))
print np.concatenate((a, b), axis=1)

print np.vstack((a, b))
print np.concatenate((a, b), axis=0)

print np.dstack((a, b))  #stack arrays in sequence depth wise(along third axis)

print np.row_stack((a, b))
print np.column_stack((a, b))
print np.column_stack((a, b)) == np.hstack((a, b))
print np.row_stack((a,b)) == np.vstack((a,b)) #False


oned = np.arange(2)
print oned
twice_oned = 2 * oned

print twice_oned
print np.row_stack((oned, twice_oned))
print np.column_stack((oned, twice_oned)) 
print np.hstack((oned, twice_oned)) 
print np.vstack((oned, twice_oned)) 
print np.row_stack((oned, twice_oned)) == np.vstack((oned, twice_oned)) 




#数组的分割
a = np.arange(9).reshape(3, 3)

print a

print np.hsplit(a, 3)

print np.split(a, 3, axis=1)

print np.vsplit(a, 3)

print np.split(a, 3, axis=0)

c = np.arange(27).reshape(3, 3, 3)

print c

print np.dsplit(c, 3)

#数组的属性
b=np.arange(24).reshape(2,12)
b.ndim
b.size
b.itemsize
b.nbytes

b = np.array([ 1.+1.j,  3.+2.j])
b.real
b.imag

b=np.arange(4).reshape(2,2)
b.flat
b.flat[2]


#数组的转换
b = np.array([ 1.+1.j,  3.+2.j])
print b

print b.tolist()

print b.tostring()

print np.fromstring('\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00@', dtype=complex)

print np.fromstring('20:42:52',sep=':', dtype=int)

print b

print b.astype(int)

print b.astype('complex')

