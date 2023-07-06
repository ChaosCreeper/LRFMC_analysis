#-*- coding:utf-8 -*-
'''
    data_zscore.py
    ~~~~~~~~~~~~~~~~~~~~~~
    客户样本数据标准化处理


'''

# 步骤1：导入模块库
import pandas as pd
import os

# 步骤：读取规约之后的样本数据集
# 步骤2：设置样本数据的路径
excelFile = os.getcwd() + '\out' + os.sep + 'data_reduction.xlsx'
# 步骤3：读取Excel数据
ef = pd.ExcelFile(excelFile)
# 步骤4：读取有效的Sheet1页并转换成数据集
data = ef.parse('Sheet1')
# 测试输出前5条数据
print('\n>>> 读取 data_reduction.xlsx数据文件，输出前5条测试数据：\n')
print(data.head())

# 步骤：进行数据标准差标准化处理
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

# 步骤：将标准化之后的数据写入到Excel文件
# excelFile = os.getcwd() + os.sep + 'out' + os.sep + 'data_zscore.xlsx'
# print('\n>>> 开始写入excel数据文件，请稍候……\n')
# # 写入excel数据文件
# data.to_excel(excelFile)
# print('\n>>>已经写入到目标过程数据集文件中.\n')

# 扩展：csv数据文件写入，会提高近15倍的速度
csvFile = os.getcwd() + os.sep + 'out' + os.sep + 'data_zscore.csv'
print('\n>>> 开始写入excel数据文件，请稍候……\n')
# 写入excel数据文件
data.to_csv(csvFile, index = False)
print('\n>>>已经写入到目标过程数据集文件中.\n')


import pandas as pd
import os

excelFile = os.getcwd() + '\out' + os.sep + 'data_reduction.xlsx'
ef = pd.ExcelFile(excelFile)
data = ef.parse('Sheet1')
print('\n>>> 读取 data_reduction.xlsx数据文件，输出前5条测试数据：\n')
print(data.head())

data = (data - data.mean(axis=0)) / data.std(axis=0)
data.columns = ['Z' + i for i in data.columns]
print('\n>>> 标准差标准化处理之后的数据样本结果为：\n')
print(data.head())

csvFile = os.getcwd() + os.sep + 'out' + os.sep + 'data_zscore.csv'
print('\n>>> 开始写入excel数据文件，请稍候……\n')
data.to_csv(csvFile, index=False)
print('\n>>>已经写入到目标过程数据集文件中.\n')