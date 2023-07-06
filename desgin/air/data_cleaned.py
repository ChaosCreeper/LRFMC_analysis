#-*- coding:utf-8 -*-
'''
    data_cleaned.py
    ~~~~~~~~~~~~~~~~~~~~~~
    实现航空数据的清洗

'''
# 步骤1：导入模块库
import pandas as pd
import os

# 步骤2：设置原始样本数据的csv文件地址
csvFile = 'air_data.csv'
# 步骤3：使用pandas中read_csv(), DataFrame数据类型
data = pd.read_csv(csvFile, encoding='ansi')
# 测试
print(data.info())

# 步骤4：筛选SUM_YR_1 和 SUM_YR_2 字段不为空的数据行（保留）
data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
# 测试
print('\n>>>根据一级条件进行筛选后的数据为：')
print(data.info())

# 步骤5：设置二级筛选条件
condtion1 = data['SUM_YR_1'] !=0
condtion2 = data['SUM_YR_2'] !=0
# 设置总里程为0和平均折扣率为0的筛选条件
condtion3 = (data['SEG_KM_SUM'] != 0) & (data['avg_discount'] == 0)
data = data[ condtion1 | condtion2 | condtion3]
# 测试
print('\n>>>根据二级条件进行筛选后的数据为：')
print(data.info())
 

# 步骤6：将explore数据写入到指定的csv文件中
csvFile = os.getcwd() + os.sep + 'out' + os.sep + 'data_cleaned.csv'
# 写入数据
data.to_csv(csvFile, encoding='utf_8_sig')
print('\n>>>数据文件写入成功.')

