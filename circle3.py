import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))

x=np.linspace(-1,1,1000)
y=np.sqrt(1-x**2)

plt.plot(x,y)
plt.plot(x,-y)

plt.show()