# -*- coding:'utf-8' -*-
'''
    data_reduction.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    实现客户行程数据规约（1/2：数据变换LRFMC）


'''

# 步骤1：导入Pandas模块
import pandas as pd
import os

# 步骤2：设置原始样本数据的csv文件地址
csvFile = './out' + os.sep + 'data_cleaned.csv'
# 步骤3：使用pandas中read_csv(), DataFrame数据类型
data = pd.read_csv(csvFile, encoding='utf-8')
# 测试
print(data.head())

# 步骤5：筛选出来6个核心属性
data = data[['FFP_DATE', 'LOAD_TIME', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM', 'LAST_TO_END']]
# 测试输出前5条数据
print('\n>>> 6项核心属性数据筛选后的前5条测试数据：')
print(data.head())

# 步骤6：根据计算公式数据转换成LRFMC模型指标
data['L'] = (pd.to_datetime(data['LOAD_TIME']) - pd.to_datetime(data['FFP_DATE'])) / 30
data['R'] = data['LAST_TO_END'] / 30
data['F'] = data['FLIGHT_COUNT']
data['M'] = data['SEG_KM_SUM']
data['C'] = data['avg_discount']
print('\n LRFMC模型数据转变之后的结果：')
print(data.head())

# 步骤7：筛选出LRFMC五个维度指标数据
data = data[['L', 'R', 'F', 'M', 'C']]
print('\n LRFMC模型数据转变之后的最终结果：')
print(data.head())

# 步骤8：将最终数据变换的样本数据集进行保存
excelFile = os.getcwd() + os.sep + 'out' + os.sep + 'data_reduction.xlsx'
print('\n>>> 开始写入到目标过程数据集文件中……请稍后')
data.to_excel(excelFile)
print('>>> 已经写入到目标过程数据集文件中.')
