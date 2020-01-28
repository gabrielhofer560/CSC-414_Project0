from skimage import io
import matplotlib.pyplot as plt
import numpy as np
I = io.imread("gigi.jpg").astype(np.float32)
I = I - 150
plt.imshow( I )
plt.show()
