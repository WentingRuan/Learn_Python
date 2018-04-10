# 1. 创建一个2*2的数组，计算对角线上元素的和
a = np.array([np.arange(2),np.arange(2)])
print(a)

#or
a = np.array([(0,1),(0,1)])
print(a)

a[0,0]+a[1,1]

# 2. 创建一个长度为9的一维数据，数组元素0到8。将它重新变为3*3的二维数组
np.array(np.arange(9)).reshape(3,3)

# 3. 创建两个3*3的数组，分别将它们合并为3*6、6*3的数组后，拆分为3个数组（维数不限定）
c = np.arange(9).reshape(3,3)
print(c)

c_rev = c[::-1,::-1]
print(c_rev)

c_new = np.array([c,c_rev])
print(c_new)

c_new.reshape(3,2,3)

# 4. 说说numpy数组的优点
"""
Numpy是专门针对数组的操作和运算进行了设计，所以数组的存储效率和输入输出性能远优于Python中的嵌套列表。
数组越大，Numpy的计算速度优势就越明显。
省掉很多循环语句，代码更加简洁，可读性更高。
"""