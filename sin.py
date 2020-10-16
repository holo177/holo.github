import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 200)
y = np.sin((3 * np.pi * 2) * t)
plt.subplot(221)
plt.title('sin((3pi/2)*t)')
plt.plot(t, y)
plt.show()