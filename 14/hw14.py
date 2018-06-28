# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:51:13 2016

@author: Administrator
"""
import pandas as pd
from sklearn.cluster import KMeans


data=pd.read_csv('d:/data/ex14.csv',index_col=0,header=0,encoding='gbk')

#k-means聚类
model = KMeans(n_clusters = 3)
model.fit(data)
 
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目'] #重命名表头
print(r)






