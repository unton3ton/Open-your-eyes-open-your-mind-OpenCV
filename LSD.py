# conda activate iWM

# https://stackoverflow.com/questions/74977491/how-can-i-apply-effects-like-a-swirl-to-a-webcam-stream-using-python-and-opencv

import numpy as np
import cv2
from skimage.transform import swirl
from PIL import Image

name = "test8.jpg"

img = cv2.imread(name)

# get dimensions
h, w = img.shape[:2]

# get center
cx = w*7 // 8 # w//2 
cy = h*7 // 8 # h//2

# set amount, number of frames and delay
max_amount = 20
dist = min(h,w)/1
angle = 0
num_frames = 50
delay = 50
border_color = (128,128,128)



# add cartoon effect
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(img, 9, 300, 300)
img = cv2.bitwise_and(color, color, mask=edges)



frames = []
# loop and increase swirl
for i in range(0,num_frames):

    # compute phase to increment over 360 degree for number of frames specified so makes full cycle
    amount = i*max_amount/num_frames

    # do swirl
    result = swirl(img, center=(cx,cy), rotation=angle, strength=amount, radius=dist, preserve_range=True).astype(np.uint8)
        
    # show result
    cv2.imwrite(f'frames/result-{i}.jpg', result)
    
    # convert to PIL format and save frames
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    pil_result = Image.fromarray(result)
    frames.append(pil_result)

# loop and decrease swirl
for i in range(0,num_frames):

    # compute phase to increment over 360 degree for number of frames specified so makes full cycle
    amount = (num_frames-i)*max_amount/num_frames

    # do swirl
    result = swirl(img, center=(cx,cy), rotation=angle, strength=amount, radius=dist, preserve_range=True).astype(np.uint8)
        
    # show result
    cv2.imwrite(f'frames/result_{i}.jpg', result)
   
    # convert to PIL format and save frames
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    pil_result = Image.fromarray(result)
    frames.append(pil_result)

# write animated gif from frames using PIL
frames[0].save(f'cartoon2_{name[:-4]}_swirl_animation.gif',save_all=True, append_images=frames[1:], optimize=False, duration=delay, loop=0)