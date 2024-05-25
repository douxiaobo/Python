# 使用参数方程画圆的Python程序

#引入numpy，调用里面的三角函数 
import numpy as np

#导入matplotlib的pyplot绘图
import matplotlib.pyplot as plt
 
#从0到2pi取200个点，2pi正好是360度的弧度，把最后一个参数200，改成1-10，自己运行看一下，就明白为什么越大越圆。
theta = np.linspace( 0 , 2 * np.pi , 200 )

#半径为1，根据需要更改半径
radius = 1

#x的坐标公式
x = radius * np.cos( theta )
#y的坐标公式
y = radius * np.sin( theta )
 
figure, axes = plt.subplots( 1 )

#绘制x,y坐标的200个点，把它们连在一起，就是个圆。 
axes.plot( x, y )
axes.set_aspect( 1 )

#标题 
plt.title( '圆的参数方程', fontproperties='STHeiti')
plt.show()
