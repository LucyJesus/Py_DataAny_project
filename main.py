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
import two
import three


print("hello world!")
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
#####################################################################


#主代码部分

two.global_all()
two.most_10b()
two.most_10d()
two.in_year_global_b_d()
two.global_b_d_r()
two.each_b_d_r()
two.combine()

three.birth_and_death_tt()
three.most_10_birth()
three.most_10_death()
three.yearly_birth_and_death_increase_plot()
three.daily_increase_plot()