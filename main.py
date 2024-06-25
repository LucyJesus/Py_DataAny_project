"""3. 数据可视化
总览图表：
	绘制全球总出生人数和总死亡人数的柱状图。
	绘制前十个出生人数和死亡人数最多的国家的柱状图。
时间序列图表：
	绘制全球每年新增出生人数和新增死亡人数的折线图。
	绘制选定几个国家的每日新增出生人数和新增死亡人数的折线图。
比较图表：
	绘制不同国家出生率和死亡率的对比图。
"""


import pandas as pd
import numpy as np
import csv
import os
import matplotlib as mp


print("hello world!")

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
#print("Script directory:", script_dir)

# 切换工作目录到脚本所在目录
os.chdir(script_dir)
#print("Current working directory after change:", os.getcwd())

# 取路径
birth = os.path.join(script_dir, 'data', 'birth.csv')
death = os.path.join(script_dir, 'data', 'death.csv')
bir_rt = os.path.join(script_dir, 'data', 'birth_rate.csv')
dea_rt = os.path.join(script_dir, 'data', 'death_rate.csv')


# 读取 CSV 文件
df_b = pd.read_csv(birth)
df_br = pd.read_csv(bir_rt)
df_d = pd.read_csv(death)
df_dr = pd.read_csv(dea_rt)
print("出生人数",'\n',df_b)
print("*********************************************************************************")
print("出生率",'\n',df_br)
print("*********************************************************************************")
print("死亡人数",'\n',df_d)
print("*********************************************************************************")
print("死亡率",'\n',df_dr)



'''print(type(df_b))
print(type(df_br))
print(type(df_d))
print(type(df_dr))'''

df = pd.DataFrame(df_b,index = [[]])