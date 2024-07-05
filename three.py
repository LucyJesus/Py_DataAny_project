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
# print("Script directory:", script_dir)

# 切换工作目录到脚本所在目录
os.chdir(script_dir)

# 规定不是国家名称的集合
exclude_list = [
    'Africa (UN)', 'Asia (UN)', 'Europe (UN)', 'Latin America and the Caribbean (UN)', 
    'Less developed regions', 'Less developed regions, excluding China', 
    'Less developed regions, excluding least developed countries', 'High-income countries', 
    'Land-locked developing countries (LLDC)', 'Least developed countries', 
    'Low-income countries', 'Lower-middle-income countries', 'More developed regions', 
    'Northern America (UN)', 'Oceania (UN)', 'Small island developing states (SIDS)', 
    'Upper-middle-income countries', 'World'
]


output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def color():
    a = random.random()
    b = random.random()
    c = random.random()
    return(a, b, c)

# 读取 CSV 文件
birth = os.path.join(script_dir, 'data', 'birth.csv')
death = os.path.join(script_dir, 'data', 'death.csv')
bir_rt = os.path.join(script_dir, 'data', 'birth_rate.csv')
dea_rt = os.path.join(script_dir, 'data', 'death_rate.csv')

df_b = pd.read_csv(birth)
df_br = pd.read_csv(bir_rt)
df_d = pd.read_csv(death)
df_dr = pd.read_csv(dea_rt)

def birth_and_death_tt():
    birth_color = color()
    death_color = color()
    df_b1 = df_b.loc[18072:18143, 'Year':'Births']
    df_d1 = df_d.loc[18072:18143, 'Year':'Deaths']
    plt.figure(figsize=(14, 7))

    plt.bar(df_b1['Year'] - 0.2, df_b1['Births'], width=0.4, color=birth_color, align='center', label='Births')
    plt.bar(df_d1['Year'] + 0.2, df_d1['Deaths'], width=0.4, color=death_color, align='center', label='Deaths')

    plt.xlabel('Year')  # 设置标题和标签
    plt.ylabel('Number')
    plt.title('World Total Births and Deaths in Year')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # 输出
    output_path = os.path.join(output_dir, '全球总出生和死亡人数的柱状图.png')
    plt.savefig(output_path)
    plt.close()


def filter_countries(df):
    return df[~df['Country name'].isin(exclude_list)]

def most_10_birth():
    # 过滤不是国家名称的条目
    flt_df = filter_countries(df_b)
    
    # 计算每个国家的总出生人数
    tt_b = flt_df.groupby('Country name')['Births'].sum().reset_index()
    tt_b = tt_b.sort_values(by='Births', ascending=False).head(10)

    # 绘制前十个出生人数最多的国家的柱状图
    plt.figure(figsize=(14, 7))
    plt.bar(tt_b['Country name'], tt_b['Births'], color=color())
    plt.xlabel('Country')
    plt.ylabel('Total Births')
    plt.title('Top 10 Countries by Total Births')
    plt.xticks(rotation=45)
    plt.grid(True)
    output_path = os.path.join(output_dir, '前十个出生人数最多的国家的柱状图.png')
    plt.savefig(output_path)


def most_10_death():
    # 过滤不是国家名称的条目
    flt_df = filter_countries(df_d)
    tt_d = flt_df.groupby('Country name')['Deaths'].sum().reset_index()
    tt_d = tt_d.sort_values(by='Deaths', ascending=False).head(10)

    # 绘制前十个死亡人数最多的国家的柱状图
    plt.figure(figsize=(14, 7))
    plt.bar(tt_d['Country name'], tt_d['Deaths'], color=color())
    plt.xlabel('Country')
    plt.ylabel('Total Deaths')
    plt.title('Top 10 Countries by Total Deaths')
    plt.xticks(rotation=45)
    plt.grid(True)
    output_path = os.path.join(output_dir, '前十个死亡人数最多的国家的柱状图.png')
    plt.savefig(output_path)


def yearly_birth_and_death_increase_plot():
    birth_color = color()
    death_color = color()
    br_yr = df_b.groupby('Year')['Births'].sum().reset_index()
    br_yr['Birth Increase'] = br_yr['Births'].diff().fillna(0)
    dt_yr = df_d.groupby('Year')['Deaths'].sum().reset_index()
    dt_yr['Death Increase'] = dt_yr['Deaths'].diff().fillna(0)

    # 绘制每年的新增出生和死亡人数折线图
    plt.figure(figsize=(14, 7))
    plt.plot(br_yr['Year'], br_yr['Birth Increase'], color=birth_color, marker='o', label='Birth Increase')
    plt.plot(dt_yr['Year'], dt_yr['Death Increase'], color=death_color, marker='x', label='Death Increase')
    plt.xlabel('Year')
    plt.ylabel('Annual Increase')
    plt.title('Global Annual Birth and Death Increase')
    plt.legend()
    plt.grid(True)

    # 输出
    output_path = os.path.join(output_dir, '全球每年新增出生和死亡人数的折线图.png')
    plt.savefig(output_path)
    plt.close()

selected_countries = ['United States', 'India', 'China']

def daily_increase_plot():
    for country in selected_countries:
        # 过滤出该国家的出生和死亡数据
        country_births = df_b[df_b['Country name'] == country].copy()
        country_deaths = df_d[df_d['Country name'] == country].copy()
        country_births['Birth Increase'] = country_births['Births'].diff().fillna(0)
        country_deaths['Death Increase'] = country_deaths['Deaths'].diff().fillna(0)

        # 绘制出生人数折线图
        plt.figure(figsize=(14, 7))
        plt.plot(country_births['Year'], country_births['Birth Increase'], color=color(), marker='o', label='Daily Birth Increase')
        plt.plot(country_deaths['Year'], country_deaths['Death Increase'], color=color(), marker='x', label='Daily Death Increase')
        plt.xlabel('Year')
        plt.ylabel('Increase')
        plt.title(f'Daily Birth and Death Increase in {country}')
        plt.legend()
        plt.grid(True)

        # 保存文件到output目录
        output_path = os.path.join(output_dir, f'{country}出生死亡人数折线图.png')
        plt.savefig(output_path)
        plt.close()


def b_d_compare(country1, country2):
    birth_color1 = color()
    death_color1 = color()
    birth_color2 = color()
    death_color2 = color()

    # 过滤出选定国家的出生率和死亡率数据
    df_br1 = df_br[df_br['Country name'] == country1].copy()
    df_dr1 = df_dr[df_dr['Country name'] == country1].copy()
    df_br2 = df_br[df_br['Country name'] == country2].copy()
    df_dr2 = df_dr[df_dr['Country name'] == country2].copy()

    plt.figure(figsize=(14, 7))

    # 绘制国家1的出生率和死亡率折线图
    plt.plot(df_br1['Year'], df_br1['Birth rate'], color=birth_color1, marker='o', linestyle='-', label=f'{country1} Birth Rate')
    plt.plot(df_dr1['Year'], df_dr1['Death rate'], color=death_color1, marker='x', linestyle='--', label=f'{country1} Death Rate')

    # 绘制国家2的出生率和死亡率折线图
    plt.plot(df_br2['Year'], df_br2['Birth rate'], color=birth_color2, marker='o', linestyle='-', label=f'{country2} Birth Rate')
    plt.plot(df_dr2['Year'], df_dr2['Death rate'], color=death_color2, marker='x', linestyle='--', label=f'{country2} Death Rate')

    plt.xlabel('Year')
    plt.ylabel('Rate')
    plt.title(f'Birth and Death Rate Comparison: {country1} vs {country2}')
    plt.legend()
    plt.grid(True)

    # 输出
    output_path = os.path.join(output_dir, f'{country1}_{country2}比较.png')
    plt.savefig(output_path)
    plt.close()

# 以下是草稿
# def yearly_birth_increase_plot():
#     # 计算每年的总出生人数
#     br_yr = df_b.groupby('Year')['Births'].sum().reset_index()
    
#     # 计算每年的新增出生人数
#     br_yr['Birth Increase'] = br_yr['Births'].diff().fillna(0)
    
#     # 绘制每年的新增出生人数折线图
#     plt.figure(figsize=(14, 7))
#     plt.plot(br_yr['Year'], br_yr['Birth Increase'], color=color(), marker='o')
#     plt.xlabel('Year')
#     plt.ylabel('Annual Birth Increase')
#     plt.title('Global Annual Birth Increase')
#     plt.grid(True)
#     output_path = os.path.join(output_dir, '全球每年新增出生人数的折线图.png')
#     plt.savefig(output_path)

# def yearly_death_increase_plot():
#     # 计算每年的总出生人数
#     br_yr = df_d.groupby('Year')['Deaths'].sum().reset_index()
    
#     # 计算每年的新增出生人数
#     br_yr['Death Increase'] = br_yr['Deaths'].diff().fillna(0)
    
#     # 绘制每年的新增出生人数折线图
#     plt.figure(figsize=(14, 7))
#     plt.plot(br_yr['Year'], br_yr['Death Increase'], color=color(), marker='o')
#     plt.xlabel('Year')
#     plt.ylabel('Annual Death Increase')
#     plt.title('Global Annual Death Increase')
#     plt.grid(True)
#     output_path = os.path.join(output_dir, '全球每年新增死亡人数的折线图.png')
#     plt.savefig(output_path)


# def birth_tt():
#     df_b1 = df_b.loc[18072:18143,'Year':'Births']
#     plt.figure(figsize=(10, 6))
#     # 绘制柱状图
#     plt.bar(df_b1['Year'], df_b1['Births'], color=color())
#     plt.xlabel('year')# 设置标题和标签
#     plt.ylabel('birth_nmb')#
#     plt.title('world_total_birth_in_year')#
#     plt.xticks(rotation=45)
#     # 显示网格线
#     plt.grid(True)
#     #输出
#     output_path = os.path.join(output_dir, '全球总出生人数的柱状图.png')
#     plt.savefig(output_path)

# def death_tt():
#     df_d1 = df_d.loc[18072:18143,'Year':'Deaths']
#     plt.figure(figsize=(10, 6))
#     # 绘制柱状图
#     plt.bar(df_d1['Year'], df_d1['Deaths'], color=color())
#     plt.xlabel('year')# 设置标题和标签
#     plt.ylabel('death_nmb')#
#     plt.title('world_total_death_in_year')#
#     plt.xticks(rotation=45)
#     plt.grid(True)
#     output_path = os.path.join(output_dir, '全球总死亡人数的柱状图.png')
#     plt.savefig(output_path)