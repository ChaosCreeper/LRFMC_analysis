#-*- coding:utf-8 -*-
'''
    data_zscore.py
    ~~~~~~~~~~~~~~~~~~~~~~
    客户样本数据标准化处理


'''

# 步骤1：导入模块库
import pandas as pd
import os

# 步骤2：设置原始样本数据的csv文件地址
csvFile = './out' + os.sep + 'data_reduction.csv'
# 步骤3：使用pandas中read_csv(), DataFrame数据类型
data = pd.read_csv(csvFile, encoding='utf_8_sig')
# 测试
print(data.head())

# 步骤4：进行数据标准差标准化处理
'''
    · 整体过程是一个典型矩阵矢量化操作
    · 每一个元素做标准差标准化处理， x = （原始值 - 均值）/ 标准值
        均值 = 数据对象.mean(axis=0)
        标准值 = 数据对象.std(axis=0)
'''
data = (data - data.mean(axis = 0)) / data.std(axis = 0)
# 重新设置一下结果集的列名称
data.columns = ['Z' + i for i in data.columns]
# 测试输出
print('\n>>> 标准差标准化处理之后的数据样本结果为：\n')
print(data.head())

# 扩展：csv数据文件写入，会提高近15倍的速度
csvFile = os.getcwd() + os.sep + 'out' + os.sep + 'data_zscore.csv'
# 写入excel数据文件
data.to_csv(csvFile, encoding='utf_8_sig', index = False)
print('\n>>>已经写入到目标过程数据集文件中.\n')


