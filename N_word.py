import numpy as np  
import matplotlib.pyplot as plt  
  
# 定义N形状的顶点坐标  
n_shape_coordinates = np.array([[0, 0], [0, 2], [1, 0], [1, 2]])  
  
# 创建一个新的图形  
plt.figure()  
  
# 绘制N形状  
plt.plot(n_shape_coordinates[:, 0], n_shape_coordinates[:, 1], marker='o')  
  
# 设置x轴和y轴的标签  
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')  
  
# 设置图形的标题  
plt.title('N Shape')  
  
# 显示网格  
plt.grid(True)  
  
# 显示图形  
plt.show()