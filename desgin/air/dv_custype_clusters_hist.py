#-*- coding:utf-8 -*-
'''
    dv_custype_clusters_hist.py
    ~~~~~~~~~~~~~~~~~~~~~~
    客户聚类统计柱状图


'''

# 步骤1：导入相关的模块
import pandas as pd
import os
# 导入Numpy模块库、Matplotlib模块库
import numpy as np   # 进行数据格式转换
import matplotlib.pyplot as plt

# 可视化中文显示设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 底层参数设置解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 底层参数设置解决正负号乱码

# 步骤2：读取标准化处理之后的原始样本数据csv文件
csvFile = './out' + os.sep + 'KMeans_clusters.csv'
# 步骤3：读取csv文件并保存到data的对象中，data对象的类型为DataFrame(Pandas重要数据类型)
data = pd.read_csv(csvFile, encoding='utf_8_sig')
# 测试输出前5条数据
print('\n>>>测试输出前5条数据结果：')
print(data.head())

# 步骤4：设置图表X轴刻度标签数据集（list列表数据类型）
x_labels = ['C' + str(i) for i in range(1, 6)]
print(x_labels)

# 步骤5：设置图表Y周标签数据集（List列表数据类型）
y_values = data.iloc[:, 0].values.tolist()
print('\n>>> Y轴数据集：')
print(type(y_values))
print(y_values)

# 步骤6：设置x、y轴的标签（Matplotlib）
# 创建一个画布
ax = plt.subplot()
# 设置Y轴显示范围
ax.set_ylim([0, 30000])
# 设置轴标签提示
ax.set_xlabel('客户类别')
ax.set_ylabel('聚类客户个数（单位：人）')
# 设置图表的标题
ax.set_title('聚类客户个数分析图')

# 步骤7：生成柱状图
bar = plt.bar(x_labels, y_values, width=0.5)
# 扩展：为每一个矩形柱添加数值标签
for x, y in zip(x_labels, y_values):
    plt.text(x, y, '%.0f' % y, ha='center', va='bottom')

# 步骤8：生成图表
plt.grid(linestyle='--')
# plt.show() # 直接显示
# 保存图片文件（jpg、svg）
imageFile = os.getcwd() + os.sep + 'out' + os.sep + 'custype_clusters_hist.jpg'
plt.savefig(imageFile)
print('\n>>>图片保存成功.')


