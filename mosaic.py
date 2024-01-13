# conda activate iWM

# https://russianblogs.com/article/3995952843/


import cv2

name = "test1.jpg"

img = cv2.imread(name, 1)
height, width, deep = img.shape

if height > width:
    d = width
else:
    d = height

mm = 21 # размер ячейки мозайки

for i in range(mm,d-mm):
    for j in range (mm,d-mm): # выбрать область для кодирования
        if i%mm == 0 and j%mm == 0:
            (b, g, r) = img[i, j]
            for n in range(0,mm):
                for m in range(0,mm):
                    img[n+i, m+j] = (b, g, r)

cv2.imwrite(f'mosaic_{name}.jpg', img)