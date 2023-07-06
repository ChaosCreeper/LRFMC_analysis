# -*- coding:utf-8 -*-
'''
    KMeans_clusters.py
    ~~~~~~~~~~~~~~~~~~~~~~
    KMeans客户聚类算法分析


'''
# 步骤1：导入模块库
import pandas as pd
import os
# pip install sklearn 指令进行安装和配置
from sklearn.cluster import KMeans

# 步骤2：读取标准化处理之后的原始样本数据csv文件
csvFile = './out' + os.sep + 'data_zscore.csv'
# 步骤3：读取csv文件并保存到data的对象中，data对象的类型为DataFrame(Pandas重要数据类型)
data = pd.read_csv(csvFile, encoding='utf_8_sig')
# 测试输出前5条数据
print('\n>>>测试输出前5条数据结果：')
print(data.head())

# 步骤4：设置聚类分析算法的分类个数参数
k = 5
# 步骤5：创建KMeans聚类模型对象实例
# n_clusters: 分类个数
kmodel = KMeans(n_clusters=k)
print('\n>>>[Success]KMeans聚类分析模型创建成功.')

# 步骤6：模型的训练
print('\n>>>已导入样本数据集，开始启动KMeans模型进行训练……')
kmodel.fit(data)
print('\n>>>[Success]KMeans模型训练完毕.')

# 步骤7：查看客户样本对应的类别个数
print('\n>>>查看客户样本对应的类别个数：')
r1 = pd.Series(kmodel.labels_).value_counts()
print(r1)

# 步骤8：查看聚类中心值
print('\n>>>查看客户样本类别的聚类标准中心值：')
r2 = pd.DataFrame(kmodel.cluster_centers_)
print(r2)

# 步骤9：连接数据形成最终统一的聚类分析统计表1 KMeans_clusters.csv
data_cluster = pd.concat([r1, r2], axis=1)
# 重新命名全新的数据集列名称
data_cluster.columns = ['聚类个数', 'ZL', 'ZR', 'ZF', 'ZM', 'ZC']
# 测试
print('\n>>>KMeans聚类统计分析表1：')
print(data_cluster)

# 步骤10：csv数据文件写入，会提高近15倍的速度
csvFile = os.getcwd() + os.sep + 'out' + os.sep + 'KMeans_clusters.csv'
# 写入excel数据文件
data_cluster.to_csv(csvFile, encoding='utf_8_sig', index=False)
print('\n>>>已经写入到目标过程数据集文件中.\n')

# 步骤11：将原始无标签数据转换为有标签数据
data_details = pd.concat([data, pd.Series(kmodel.labels_, index=data.index)], axis=1)
# 重新命名全新的数据集列名称
data_details.columns = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC', '客户类别']
# 测试
print('\n>>>KMeans客户分类明细统计表2：')
print(data_details)

# 步骤10：csv数据文件写入，会提高近15倍的速度
csvFile = os.getcwd() + os.sep + 'out' + os.sep + 'KMeans_clusters_details_data.csv'
# 写入excel数据文件
data_details.to_csv(csvFile, encoding='utf_8_sig', index=False)
print('\n>>>已经写入到目标过程数据集文件中.\n')


