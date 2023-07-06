#-*- coding:utf-8 -*-
'''
    dv_custype_features_radar.py
    ~~~~~~~~~~~~~~~~~~~~~~
    客户聚类特征值分布雷达图

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

# 步骤4：为数据添加新列（客户类别名称）
customers_names = pd.Series(['C' + str(i) for i in range(1, 6)])
# 连接两个数据集形成雷达图所需的基础数据结构
data = pd.concat([customers_names, data], axis=1)
# 重新设置数据集列标题名称
data.columns = ['类别名称', '聚类个数', 'ZL:客户关系长度', 'ZR:消费时间间隔',
                'ZF:消费频率', 'ZM:飞行里程', 'ZC:平均折扣系数']
# 测试
print('\n>>>整理之后的数据集结果：')
print(data)

# 步骤5：获取客户类别名称数据集
kinds = data.iloc[:, 0]
print('\n>>> kinds:')
print(kinds)

# 步骤6：获取特征值数据矩阵
centers = data.iloc[:, 2:].values
print('\n>>> centers:')
print(centers)

# 步骤7：获取特征值的字段名称数据集（用于设置标签名称）
labels = data.iloc[:, 2:].columns
n = len(labels)  # n个角

# 步骤8：设置雷达图的基础底线结构
angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
angles = np.concatenate((angles, [angles[0]]))

print(f"angles:{angles}\nn:{n}")
# 步骤9：开始设置画布
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)  # 设置作为极点坐标
# 画若干个五边形
floor = np.floor(centers.min())  # 最小值
ceil = np.ceil(centers.max())  # 最大值
for i in np.arange(floor, ceil + 0.5, 0.5):
    ax.plot(angles, [i] * (n + 1), '--', lw=0.5, color='black')

# 去掉背景的圆圈
ax.spines['polar'].set_visible(False)  # 去掉外圈
ax.grid()  # 去掉内圈
ax.set_yticks([])  # 去掉原始刻度
# 设置极点方向
ax.set_theta_zero_location('N')  # 设置极标坐标的起点为0，即正北方向。
# 设置显示标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# 绑定数据
for i in range(len(kinds)):
    ax.plot(angles, np.concatenate((centers[i], [centers[i][0]])), lw=2, label=kinds[i])

# 添加图例
plt.legend(loc='lower right', bbox_to_anchor=(1.1, 0.1))

# 步骤10：保存图片文件（jpg、svg）
imageFile = os.getcwd() + os.sep + 'out' + os.sep + 'custype_clusters_features_radar.jpg'
plt.savefig(imageFile)
print('\n>>>图片保存成功.')


