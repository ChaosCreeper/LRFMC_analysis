import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.DataFrame({'sports': ['力量', '速度', '力量', '敏捷', '耐力', '分析才能'], 'values': [7, 8, 6, 10, 8, 9]})

fig = plt.figure()

ax = fig.add_subplot(111, projection="polar")

theta = np.arange(len(df) + 1) / float(len(df)) * 2 * np.pi

values = df['values'].values
values = np.append(values, values[0])

l1, = ax.plot(theta, values, color="purple", marker="o", label="Name of values")

ax.tick_params(pad=10)
ax.fill(theta, values, 'green', alpha=0.3)

plt.show()