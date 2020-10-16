import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 100)  # 把 0 - 6   100等分
y = np.cos(2 * np.pi * x) * np.exp(-x) + 0.8  #  构造函数
plt.plot(x, y ,label='cos(2*Pi*x)*(1/e)^x + 0.8',color='red', linewidth=3)
plt.title('plot图')  # 标题
plt.xlabel('x')   # x轴标题
plt.ylabel('y')  # y轴标题
plt.legend()  #  设置图注
plt.show()     # 显示这个图标
