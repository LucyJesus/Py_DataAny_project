# 2. 数据分析
# 总览分析：
# 	计算全球出生和总死亡人数。
# 	计算各国的总出生人数和总死亡人数。
# 	找出出生人数和死亡人数最多的前十个国家。
# 时间序列分析：
# 	分析全球每年出生人数和死亡人数的变化趋势。
# 	分析选定几个国家（如美国、印度、巴西等）的每年出生人数和死亡人数的变化趋势。
# 统计分析：
# 	使用NumPy计算全球和各国的出生率和死亡率。
# 	计算选定几个国家的基本统计数据（如均值、中位数、方差等）。



import pandas as pd
import os

# 读取CSV文件
deaths_df = pd.read_csv(r'data/birth.csv')
births_df = pd.read_csv(r'data/death.csv')
population_df = pd.read_csv(r'data/population.csv')

# 合并数据帧
df = pd.merge(births_df, deaths_df, on=['Country name', 'Year'], how='inner')
df = pd.merge(df, population_df, on=['Country name', 'Year'], how='inner')

# 去除列名中的空格
df.columns = df.columns.str.strip()

# 检查缺失值并填充
df.fillna(0, inplace=True)

# 确认数据类型并转换
df['Births'] = df['Births'].astype(int)
df['Deaths'] = df['Deaths'].astype(int)
df['Population'] = df['Population'].astype(int)

# 总出生死亡人数
global_births = df['Births'].sum()
global_deaths = df['Deaths'].sum()

# 创建输出目录
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, '第二题输出文件.txt')

def global_all():
    with open(output_path, 'w+') as f:
        f.write(f"全球总出生: {global_births}\n")
        f.write(f"总死亡: {global_deaths}\n")

# 按国家计算总出生人数和总死亡人数
country_totals = df.groupby('Country name')[['Births', 'Deaths', 'Population']].sum()

# 过滤掉非国家实体
exclude_list = [
    'Africa (UN)', 'Asia (UN)', 'Europe (UN)', 'Latin America and the Caribbean (UN)', 
    'Less developed regions', 'Less developed regions, excluding China', 
    'Less developed regions, excluding least developed countries', 'High-income countries', 
    'Land-locked developing countries (LLDC)', 'Least developed countries', 
    'Low-income countries', 'Lower-middle-income countries', 'More developed regions', 
    'Northern America (UN)', 'Oceania (UN)', 'Small island developing states (SIDS)', 
    'Upper-middle-income countries', 'World'
]

country_totals = country_totals[~country_totals.index.isin(exclude_list)]

# 找出出生人数最多的前十个国家
def most_10b():
    top10_births = country_totals['Births'].nlargest(10)
    with open(output_path, 'a') as f:
        f.write("出生人数最多的前十个国家:\n")
        f.write(f"{top10_births}\n")

# 找出死亡人数最多的前十个国家
def most_10d():
    top10_deaths = country_totals['Deaths'].nlargest(10)
    with open(output_path, 'a') as f:
        f.write("死亡人数最多的前十个国家:\n")
        f.write(f"{top10_deaths}\n")

# 按年份计算全球每年出生人数和死亡人数
def in_year_global_b_d():
    annual_global_totals = df.groupby('Year')[['Births', 'Deaths']].sum()
    with open(output_path, 'a') as f:
        f.write("按年份计算全球每年出生人数和死亡人数:\n")
        f.write(f"{annual_global_totals}\n")

# 选择要分析的国家
selected_countries = ['United States', 'India', 'Brazil']
annual_country_totals = df[df['Country name'].isin(selected_countries)].groupby(['Year', 'Country name'])[['Births', 'Deaths']].sum().reset_index()

# 计算全球出生率和死亡率
def global_b_d_r():
    global_birth_rate = global_births / df['Population'].sum() * 1000
    global_death_rate = global_deaths / df['Population'].sum() * 1000
    with open(output_path, 'a') as f:
        f.write(f"Global birth rate: {global_birth_rate:.2f} per 1000 people\n")
        f.write(f"Global death rate: {global_death_rate:.2f} per 1000 people\n")

# 计算各国出生率和死亡率
def each_b_d_r():
    country_totals['birth_rate'] = country_totals['Births'] / country_totals['Population'] * 1000
    country_totals['death_rate'] = country_totals['Deaths'] / country_totals['Population'] * 1000
    with open(output_path, 'a') as f:
        f.write("各国出生率和死亡率:\n")
        f.write(f"{country_totals[['birth_rate', 'death_rate']]}\n")

# 计算选定国家的基本统计数据
def combine():
    selected_country_stats = df[df['Country name'].isin(selected_countries)]
    country_stats = selected_country_stats.groupby('Country name')[['Births', 'Deaths']].agg(['mean', 'median', 'var'])
    with open(output_path, 'a') as f:
        f.write("选定国家的基本统计数据:\n")
        f.write(f"{country_stats}\n")
