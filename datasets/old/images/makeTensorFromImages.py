'''
Builds a np tensor out of a bunch of images of a Car
'''

import cv2
import numpy as np

#In a rush so this is gonna be ugly.


tensor = np.zeros((128, 128, 128))

for imgIdx in range(0, 128):
    im = cv2.imread("img_"+str(imgIdx)+".png",flags=cv2.IMREAD_GRAYSCALE)
    tensor[:, imgIdx, :] = im[:, :]
np.savez_compressed('boats.npz', tensor)
