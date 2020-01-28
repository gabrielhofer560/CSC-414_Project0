import time
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float32
import sys

def process(file):
  A = io.imread(file)
  (m1,n1) = A.shape
  for i in range(m1):
    for j in range(n1):
      if A[i,j] <= 80 :
        A[i,j] = 0

start = time.time()
for file in sys.argv[1:]:
  process(file)
end = time.time()
print("total time: "+str(end - start))

