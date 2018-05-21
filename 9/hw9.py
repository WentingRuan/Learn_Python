# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:08:15 2016

@author: Administrator
"""

import pandas as pd
from scipy import stats as ss

'''
1
(1)零假设：罐装可口可乐的标准差为0.005磅
备择假设：罐装可口可乐的标准差不为0.005磅
（2）零假设：中国的离婚率为38.5%
备择假设：中国的离婚率低于38.5%
（3）零假设：该学校的学生就业率为99%
备择假设：该学校的学生就业率低于99%
'''

#2
tmp2=pd.Series([3.2,3.3,3.0,3.7,3.5,4.0,3.2,4.1,2.9,3.3])
ss.ttest_1samp(a=tmp2,popmean=3.5)

#3
tmp3=pd.ExcelFile('d:/data/Amtrak.xls')
tmp4=tmp3.parse('Data',parse_cols='A,B')
tmp4.describe()

tmp4.var()

tmp4.skew()

tmp4.kurt()
