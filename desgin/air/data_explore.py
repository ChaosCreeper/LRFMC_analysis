#-*- coding:utf-8 -*-
'''
    data_explore.py
    ~~~~~~~~~~~~~~~~~~~~~~
    实现航空数据的探索

'''
# 步骤1：导入模块库
import pandas as pd
import os

# 步骤2：设置原始样本数据的csv文件地址
csvFile = 'air_data.csv'
# 步骤3：使用pandas中read_csv(), DataFrame数据类型
data = pd.read_csv(csvFile, encoding='ansi')
# 测试
print(data.head())

# 步骤4：获取数据中的空值项，并进行转置处理
explore = data.describe(percentiles=[], include='all').T
# 测试
print('\n数据描述统计结果：')
print(explore)

# 步骤5：计算每个属性的空值个数
explore['null'] = len(data) - explore['count']
# 步骤6：梳理最终数据探索的表格显示结构
explore = explore[['null', 'max', 'min']]
# 步骤7：设置最终数据的标题字段名称
explore.columns = ['空值数', '最大值', '最小值']
# 测试
print('\n最终探索的数据结果为：')
print(explore)

# 步骤8：将最终的结果写入到指定的文件当中去
csvPath = os.getcwd() + os.sep + 'out'
# 判断如果不存在则自动创建
if not os.path.exists(csvPath):
    print('\n>>>程序检测到指定输出文件夹不存在，正在创建中……')
    os.makedirs(csvPath)
    print('\n>>>输出文件夹创建成功.')

# 步骤9：将explore数据写入到指定的csv文件中
csvFile = csvPath + os.sep + 'data_explore.csv'
# 写入数据
explore.to_csv(csvFile, encoding='utf_8_sig')
print('\n>>>数据文件写入成功.')




