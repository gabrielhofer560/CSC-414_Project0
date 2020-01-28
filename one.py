### Gabriel Hofer
### Project 0: Using Python for Image Manipulation
### Due: Monday Jan 27, 2020
### Instructor: Dr. Hoover
###

import time
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


# start the timer
start = time.time()

# read the image
A = io.imread("grizzlypeakg.png")
(m1,n1) = A.shape

plt.imshow(A)
plt.show()



# logical indexing to set values less than 10 to 0


B = A < 100
A[B] = 0

# display the image after changes
plt.imshow(A)
plt.show()


# stop the timer and display elapse time to modify image
end = time.time()
print("total time: "+str(end - start))



