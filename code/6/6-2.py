# -*- coding:utf-8 -*-
from bokeh.plotting import figure, output_file, show
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
# 输出为静态文件
output_file("lines.html", title="line plot example")
# 创建一个figure对象，附带标题和坐标轴标记
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
# 添加一条线，设置图例
p.line(x, y, legend="Line A.", line_width=2)
show(p)
