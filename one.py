import pandas as pd
import os

# 打印当前工作目录
# print(os.getcwd())

# 确保文件路径正确
def clean():
    population_path = "data/population-and-demography.csv"
    birth_path = "data/population-and-demography (1).csv"
    death_path = "data/population-and-demography (2).csv"
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 读取文件
    population = pd.read_csv(population_path)  # 读取总人口数数据
    birth = pd.read_csv(birth_path)   # 读取出生人口数据
    death = pd.read_csv(death_path)   # 读取死亡人口数据
    #下面进行数据清洗和整理无效数据
    data1 = population.loc[:,'Country name':'Population']    #去年龄段 保留总人口数
    list1= data1['Country name'].tolist()
    list2=data1['Year'].tolist()
    list3= data1['Population'].tolist()
    s= {'Year':list2,'Population':list3}
    data_Population = pd.DataFrame(s,[list1])              #转换国家或地区为行标签

    data2 = birth.loc[:,'Country name':'Births']    #同理 出生人数
    list1= data2['Country name'].tolist()
    list2=data2['Year'].tolist()
    list3= data2['Births'].tolist()
    s= {'Year':list2,'Births':list3}
    data_Birth = pd.DataFrame(s,[list1]) 

    data3 = death.loc[:,'Country name':'Deaths']  #死亡人数
    list1= data3['Country name'].tolist()
    list2=data3['Year'].tolist()
    list3= data3['Deaths'].tolist()
    s= {'Year':list2,'Deaths':list3}
    data_Death = pd.DataFrame(s,[list1]) 

    # print(data_Population.isnull().sum())  #检查是否有缺失值
    # print(data_Population.duplicated())    #检查是否有重复行
    # print(data_Population.dtypes)          #检查数据类型

    # print(data_Birth.isnull().sum())  #检查是否有缺失值
    # print(data_Birth.duplicated())    #检查是否有重复行
    # print(data_Birth.dtypes)          #检查数据类型
    data_Birth['Births']=data_Birth['Births'].astype('int64')   #修改数据类型为整形
    # print(data_Birth.dtypes)          #再次检查

    # print(data_Death.isnull().sum())  #检查是否有缺失值
    # print(data_Death.duplicated())    #检查是否有重复行
    # print(data_Death.dtypes)          #检查数据类型

    # print(data_Population)
    # print(data_Birth)
    # print(data_Death)
    # 指定输出文件路径
    population_output_path = os.path.join(output_folder, '人口数据(已清洗).csv')
    birth_output_path = os.path.join(output_folder, '出生数据(已清洗).csv')
    death_output_path = os.path.join(output_folder, '死亡数据(已清洗).csv')

    # 输出为csv文件
    data_Population.to_csv(population_output_path, index=False)
    data_Birth.to_csv(birth_output_path, index=False)
    data_Death.to_csv(death_output_path, index=False)