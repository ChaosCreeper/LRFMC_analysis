#-*- coding:utf-8 -*-
'''
    data_reduction.py
    ~~~~~~~~~~~~~~~~~~~~~~
    数规约&转换

'''
# 步骤1：导入模块库
import pandas as pd
import os

# 步骤2：设置原始样本数据的csv文件地址
csvFile = './out' + os.sep + 'data_cleaned.csv'
# 步骤3：使用pandas中read_csv(), DataFrame数据类型
data = pd.read_csv(csvFile, encoding='utf_8_sig')
# 测试
print(data.head())

# 步骤4：筛选出6个核心的属性字段数据集
data = data[['FFP_DATE', 'LOAD_TIME', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM', 'LAST_TO_END']]
# 测试输出
print('\n>>>测试输出核心属性字段数据集：')
print(data)

# 步骤5：计算公式讲现有数据转换成LRFMC指标格式
data['L'] = [i.days for i in (pd.to_datetime(data['LOAD_TIME']) - pd.to_datetime(data['FFP_DATE']))/30]
data['R'] = data['LAST_TO_END']/30
data['F'] = data['FLIGHT_COUNT']
data['M'] = data['SEG_KM_SUM']
data['C'] = data['avg_discount']

# 步骤6：筛选出LRFMC五个维度指标
data = data[['L', 'R', 'F', 'M', 'C']]
#测试
print('\n>>>数据规约转换之后的结果：')
print(data.head())

# 步骤7：将explore数据写入到指定的csv文件中
csvFile = os.getcwd() + os.sep + 'out' + os.sep + 'data_reduction.csv'
# 写入数据
data.to_csv(csvFile, encoding='utf_8_sig', index = False)
print('\n>>>数据文件写入成功.')