#3. 数据可视化
#总览图表：
#	绘制全球总出生人数和总死亡人数的柱状图。
#	绘制前十个出生人数和死亡人数最多的国家的柱状图。
#时间序列图表：
#	绘制全球每年新增出生人数和新增死亡人数的折线图。
#	绘制选定几个国家的每日新增出生人数和新增死亡人数的折线图。
#比较图表：
#	绘制不同国家出生率和死亡率的对比图。


import os
import one as o
import two_1 as tw
import three as tr


print("hello world!")
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
#####################################################################


#主代码部分
o.clean()

tw.global_all()
tw.most_10b()
tw.most_10d()
tw.in_year_global_b_d()
tw.global_b_d_r()
tw.each_b_d_r()
tw.combine()

tr.birth_and_death_tt()
tr.most_10_birth()
tr.most_10_death()
tr.yearly_birth_and_death_increase_plot()
tr.daily_increase_plot()
tr.b_d_compare('United States', 'China')