import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1) # 0から6まで0.1刻み
y = np.sin(x)

plt.plot(x,y)
plt.show()
