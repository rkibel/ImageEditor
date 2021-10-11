import numpy as np 
from imageio import imread, imwrite 
import cv2
img1 = imread('EiffelTower.jpg')
img2 = cvread('EiffelTower.jpg')
arr1 = img * np.array([0.1, 0.2, 0.5])
arr2 = (255+arr1/arr1.max()).astype(np.uint8)
imwrite('night.jpg')
gamma = 3
gamma_img = np.array(255*(img2/255))
gamma, dtype = 'uint8'
cv2.imwrite('night_final.jpg', gamma_img)


