import matplotlib.pyplot as plt
 
# 设置圆的中心和半径
x_center, y_center = 1, 1
radius = 3

fig,ax=plt.subplots()


# 绘制圆
# plt.subplot(111)
circle=plt.Circle((x_center, y_center), radius, color='blue', fill=False)

ax.add_artist(circle)

ax.set_aspect('equal', adjustable='datalim')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Plotting a Circle using matplotlib')
ax.grid(True)

plt.plot(x_center,y_center,'o')

# 显示坐标轴
# plt.axis('equal')
 
# 显示图形
plt.show()