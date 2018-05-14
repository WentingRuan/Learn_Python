# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:12:09 2016

@author: Administrator
"""

import numpy as np
#1
tmp1=np.loadtxt('d:/data/ag0613.csv', delimiter=',',skiprows=(1))
print tmp1

print tmp1.max()
print tmp1.min()
print tmp1.mean()
print tmp1.std()
print np.median(tmp1)

#2
a=np.array([[1,2],[3,4]])
b=np.array([[2,5],[1,3]])
tmp2=a.dot(b)
print tmp2

#3
tmp3=np.random.normal(size=100)
print tmp3.mean()
print tmp3.std()