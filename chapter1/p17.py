import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('test.jpeg')
plt.imshow(img)

plt.show()