# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:36:30 2016

@author: Administrator
"""

import numpy as np
import pandas as pd

file = pd.ExcelFile("d:/data/ApplianceShipments.xls")
tmp1=file.parse('Data')
print tmp1
tmp1=tmp1.iloc[:,:2]
tmp1
tmp2=pd.read_table('d:/data/creditcard-dataset.txt', sep=',',header=None)
print tmp2
tmp3 = pd.read_csv('d:/data/Dress Sales.csv')
tmp3