# Read in original RGB image.
import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt
rgbImage = io.imread(’yourimage.jpg’)
(m,n,o) = rgbImage.shape
# Extract color channels.
redChannel = rgbImage[:,:,0] # Red channel
greenChannel = rgbImage[:,:,1] # Green channel
blueChannel = rgbImage[:,:,2] # Blue channel
# Create an all black channel.
allBlack = np.zeros((m, n), dtype=np.uint8)
# Create color versions of the individual color channels.
justRed = np.stack((redChannel, allBlack, allBlack), axis=2)
justGreen = np.stack((allBlack, greenChannel, allBlack),axis=2)
justBlue = np.stack((allBlack, allBlack, blueChannel),axis=2)
# Recombine the individual color channels to create the original RGB image
again.
recombinedRGBImage = np.stack(( redChannel, greenChannel, blueChannel),axis=2)
plt.imshow(recominedRGBImage)
plt.show()




