# conda activate iWM

# https://pysource.com/2018/10/11/how-to-create-a-cartoon-effect-opencv-with-python/

import cv2
import numpy as np

def inverte(image, name):
    image = 255-image
    cv2.imwrite(name, imagem)

name = "test7.jpg"

img = cv2.imread(name)

# 1) Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 2) Color
color = cv2.bilateralFilter(img, 9, 300, 300)

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imwrite(f"Cartoon-{name[:-4]}.jpg", cartoon)
cv2.imwrite(f"edges-{name[:-4]}.jpg", edges)

inverted_image = np.invert(edges)
cv2.imwrite(f"InvertedImage-{name[:-4]}.jpg", inverted_image)