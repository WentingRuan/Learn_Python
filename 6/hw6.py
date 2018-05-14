# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:36:41 2016

@author: Administrator
"""
import pandas as pd
import numpy as np
from scipy.interpolate import lagrange

#1
data1 = pd.read_excel('C:/Users/41914/Documents/Language/new/learn_python/Learn_Python/6/hw_data/肝气郁结证型系数.xls') 
data1.head()

data1['group1']=pd.cut(data1[u'肝气郁结证型系数'],5)

data1.groupby(['group1'])[u'肝气郁结证型系数'].median()
data1.groupby(['group1'])[u'肝气郁结证型系数'].std()

data1['group2']=pd.qcut(data1[u'肝气郁结证型系数'],5)

data1.groupby(['group2'])[u'肝气郁结证型系数'].median()
data1.groupby(['group2'])[u'肝气郁结证型系数'].std()


#2
data2=pd.read_csv("C:/Users/41914/Documents/Language/new/learn_python/Learn_Python/6/hw_data/BHP1.csv")
data2

data2=data2.iloc[:,:-1]
data2

def ployinterp_column(s, n, k=3):
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
  y = y[y.notnull()] #剔除空值
  return lagrange(y.index, list(y))(n) #插值并返回插值结果

for i in data2.columns:
  for j in range(len(data2)):
    if (data2[i].isnull())[j]: #如果为空即插值。
      data2[i][j] =ployinterp_column(data2[i],j)
      
#3
data3=pd.read_excel("C:/Users/41914/Documents/Language/new/learn_python/Learn_Python/6/hw_data/BHP2.xlsx")
data3

BHP=pd.merge(data2,data3,how='outer')
BHP

#4
data4=BHP.copy()
q1=data4['volume'].quantile(0.25)
q3=data4['volume'].quantile(0.75)

def trans(x):
    if x<q1:
        x='low'
    elif (x>=q1)&(x<=q3):
        x='median'
    elif x>q3:
        x='high'
    return x
    
data4=data4['volume'].map(trans)
        

