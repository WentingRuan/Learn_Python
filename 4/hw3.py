# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:44:12 2016

@author: Administrator
"""

import numpy as np

#1
tmp1=np.array([[1,2],[3,4]])
print tmp1
print sum(np.diag(tmp1))

#2
tmp2=np.arange(9)
print tmp2
tmp2_2=tmp2.reshape(3,3)
print tmp2_2

#3
tmp3_1=np.arange(9).reshape(3,3)
tmp3_2=np.arange(9).reshape(3,3)

tmp3_3=np.concatenate((tmp3_1,tmp3_2),axis=1)
tmp3_4=np.concatenate((tmp3_1,tmp3_2),axis=0)

tmp3_5=np.hsplit(tmp3_4,3)

print tmp3_1
print tmp3_2
print tmp3_3
print tmp3_4
print tmp3_5
