import skimage
from skimage import io
import numpy as np
A = io.imread("gigi.jpg")
(m1,n1) = A.shape

# this method uses logical indexing
B = A < 10
A[B] = 0





