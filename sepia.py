# conda activate iWM

# https://datahacker.rs/004-how-to-smooth-and-sharpen-an-image-in-opencv/
# https://dev.to/ethand91/creating-more-filters-with-opencv-and-python-3bhh

# https://sanstv.ru/color#394304
# https://www.codespeedy.com/color-filtering-with-opencv-in-python/

import cv2
import numpy as np

def style(image):
    image_blur = cv2.GaussianBlur(image, (5, 5), 0, 0)
    image_style = cv2.stylization(image_blur, sigma_s = 40, sigma_r = 0.1)

    return image_style

name = "test11.jpg"

img = cv2.imread(name)



# Creating our sepia filter
filter = np.array([[0.272, 0.534, 0.131],
                   [0.349, 0.686, 0.168],
                   [0.393, 0.769, 0.189]])

# Applying cv2.transform function
sepia_img=cv2.transform(img,filter)

cv2.imwrite(f"sepia-{name[:-4]}.jpg", sepia_img)


cv2.imwrite(f"Style_Filter-{name[:-4]}.jpg", style(sepia_img))


# Creating our arbitrary filter
filter = np.array([[3, -2, -3], [-4, 8, -6], [5, -1, -0]])

# Applying cv2.filter2D on our Cybertruck image
custom_img_1=cv2.filter2D(img,-1,filter)

cv2.imwrite(f"Mexican_hat_or_Laplacian_filter-{name[:-4]}.jpg", custom_img_1)

custom_img_1=cv2.filter2D(sepia_img,-1,filter)
cv2.imwrite(f"Mexican_hat_and_sepia-{name[:-4]}.jpg", custom_img_1)



# Color filtering

name = "eyes.jpg"

img = cv2.imread(name)

lower_range = np.array([0,0,0])  # Set the Lower range value of color in BGR
upper_range = np.array([10,75,65])   # Set the Upper range value of color in BGR
mask = cv2.inRange(img,lower_range,upper_range) # Create a mask with range
result = cv2.bitwise_and(img,img,mask = mask)  # Performing bitwise and operation with mask in img variable

bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converting the Orginal image to Gray
bw_bgr = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR) # Converting the Gray image to BGR format
result2 = cv2.bitwise_or(bw_bgr, result) # Performing Bitwise OR operation with gray bgr image and previous result image

cv2.imwrite(f"Color_filtering-{name[:-4]}.jpg", result2)  # Showing The Final Result Image
