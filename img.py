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
import matplotlib.pyplot as plt
import random


#print("hello world!")

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Script directory:", script_dir)

# 切换工作目录到脚本所在目录
os.chdir(script_dir)

def color():
    a = random.random()
    b = random.random()
    c = random.random()
    return(a,b,c)



birth = os.path.join(script_dir, 'data', 'birth.csv')
death = os.path.join(script_dir, 'data', 'death.csv')
bir_rt = os.path.join(script_dir, 'data', 'birth_rate.csv')
dea_rt = os.path.join(script_dir, 'data', 'death_rate.csv')


# 读取 CSV 文件
df_b = pd.read_csv(birth)
df_br = pd.read_csv(bir_rt)
df_d = pd.read_csv(death)
df_dr = pd.read_csv(dea_rt)

#print(df_b,df_b.index,df_b.columns,sep = '\n')

def birth_tt():
    df_b1 = df_b.loc[18072:18143,'Year':'Births']
    plt.figure(figsize=(10, 6))
    # 绘制柱状图
    plt.bar(df_b1['Year'], df_b1['Births'], color=color())
    plt.xlabel('year')# 设置标题和标签
    plt.ylabel('birth_nmb')#
    plt.title('world_total_birth_in_year')#
    plt.xticks(rotation=45)
    # 显示网格线
    plt.grid(True)
    #输出
    plt.savefig('world_total_birth_in_year.png')

def death_tt():
    df_d1 = df_d.loc[18072:18143,'Year':'Deaths']
    plt.figure(figsize=(10, 6))
    # 绘制柱状图
    plt.bar(df_d1['Year'], df_d1['Deaths'], color=color())
    plt.xlabel('year')# 设置标题和标签
    plt.ylabel('death_nmb')#
    plt.title('world_total_death_in_year')#
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig('world_total_death_in_year.png')


def most_10_birth():
    # 计算每个国家的总出生人数
    total_births = df_b.groupby('Country name')['Births'].sum().reset_index()
    total_births = total_births.sort_values(by='Births', ascending=False).head(20)

    # 绘制前十个出生人数最多的国家的柱状图
    plt.figure(figsize=(14, 7))
    plt.bar(total_births['Country name'], total_births['Births'], color=color())
    plt.xlabel('Country')
    plt.ylabel('Total Births')
    plt.title('Top 10 Countries by Total Births')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig('world_most_10_birth_in_year.png')

def most_10_death():
    # 计算每个国家的总死亡人数
    total_deaths = df_d.groupby('Country name')['Deaths'].sum().reset_index()
    total_deaths = total_deaths.sort_values(by='Deaths', ascending=False).head(20)

    # 绘制前十个死亡人数最多的国家的柱状图
    plt.figure(figsize=(14, 7))
    plt.bar(total_deaths['Country name'], total_deaths['Deaths'], color=color())
    plt.xlabel('Country')
    plt.ylabel('Total Deaths')
    plt.title('Top 10 Countries by Total Deaths')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig('world_most_10_death_in_year.png')

'''
def most_nmb(x):
    a = x.loc[]'''


'''def birth_rt():'''
	
'''
def death_rt():'''

