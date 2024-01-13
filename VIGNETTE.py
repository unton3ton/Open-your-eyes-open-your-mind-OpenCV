# conda activate iWM

# https://www.geeksforgeeks.org/create-a-vignette-filter-using-python-opencv/


import numpy as np
import cv2


name = 'test1.jpg'
	
#reading the image 
input_image = cv2.imread(name)

#resizing the image according to our need 
# resize() function takes 2 parameters, 
# the image and the dimensions 

input_image = cv2.resize(input_image, (480, 480))

# Extracting the height and width of an image 
rows, cols = input_image.shape[:2]

# generating vignette mask using Gaussian 
# resultant_kernels
X_resultant_kernel = cv2.getGaussianKernel(cols,200)
Y_resultant_kernel = cv2.getGaussianKernel(rows,200)

#generating resultant_kernel matrix 
resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T

#creating mask and normalising by using np.linalg
# function
mask = 255 * resultant_kernel / np.linalg.norm(resultant_kernel)
output = np.copy(input_image)

# applying the mask to each channel in the input image
for i in range(3):
	output[:,:,i] = output[:,:,i] * mask
	

cv2.imwrite(f'VIGNETTE_{name}.jpg', output)