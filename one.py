import time
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float32
import sys

# start the timer
start = time.time()

def process(file):
  A = io.imread(file)
  (m1,n1) = A.shape
  
  plt.imshow(A)
  plt.show()
  
  # logical indexing to set values less than 10 to 0
  B = A < 80
  A[B] = 0
  
  # display the image after changes
  plt.imshow(A)
  plt.show()
  
  # stop the timer and display elapse time to modify image
  end = time.time()
  print("total time: "+str(end - start))

# read the image
for file in sys.argv[1:]:
  process(file)



