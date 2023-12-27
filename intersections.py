import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


def center_image(img1):
    #Image Centering

    # hh, ww = img1.shape
    hh = img1.shape[0]
    ww = img1.shape[1]


    # get contours (presumably just one around the nonzero pixels) 
    contours = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)

    # recenter
    startx = (ww - w)//2
    starty = (hh - h)//2
    result = np.zeros_like(img1)
    result[starty:starty+h,startx:startx+w] = img1  [y:y+h,x:x+w]
    return result



def calculate_intersections(path):
    img1 = cv2.imread(path)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img1 = cv2.threshold(img1, 1, 255, cv2.THRESH_BINARY)
    img1 = center_image(img1)
    plt.imshow(img1, cmap='gray')

    x = img1.shape[0]
    y = img1.shape[1]

    ## To draw horizontal lines

    horizotal_lines = np.zeros_like(img1, dtype = np.uint8)

    horizotal_lines = cv2.line(horizotal_lines, (0, 28), (x, 28), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 42), (x, 42), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 55), (x, 55), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 69), (x, 69), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 82), (x, 82), (255, 255, 255), 1)

    ## To draw vertical lines

    vertical_lines = np.zeros_like(img1, dtype = np.uint8)

    vertical_lines = cv2.line(vertical_lines, (28, 0), (28, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (42, 0), (42, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (55, 0), (55, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (69, 0), (69, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (82, 0), (82, y), (255, 255, 255), 1)


    ## Get Intersection points
    horizontal_intersections = horizotal_lines & img1
    vertical_intersections = vertical_lines & img1

    horizontal_count = 0
    vertical_count = 0

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if horizontal_intersections[i][j] > 230:
                horizontal_count += 1
            if vertical_intersections[i][j] > 230:
                vertical_count += 1
    return horizontal_count, vertical_count

current_num = 5

num1h, num1v = calculate_intersections(f"NumberData/Number{current_num}/num1.jpg")
num2h, num2v = calculate_intersections(f"NumberData/Number{current_num}/num2.jpg")
num4h, num4v = calculate_intersections(f"NumberData/Number{current_num}/num4.jpg")
num6h, num6v = calculate_intersections(f"NumberData/Number{current_num}/num6.jpg")
num9h, num9v = calculate_intersections(f"NumberData/Number{current_num}/num9.jpg")
num11h, num11v = calculate_intersections(f"NumberData/Number{current_num}/num11.jpg")
num14h, num14v = calculate_intersections(f"NumberData/Number{current_num}/num14.jpg")

total_horizontal =   num1h  + num2h+ num4h +num6h+ num9h + num11h + num14h 
total_vertical =     num1v + num2v+ num4v + num9v + num11v + num6v + num14h

avg_horizontal = total_horizontal // 7
avg_vertical = total_vertical // 7
print(f"Average Horizontal Lines: {avg_horizontal}")
print(f"Average Vertical Lines: {avg_vertical}")


###
# 1: 11, 16      20 , 20
# 2: 22, 26      26 , 26
# 3: 22 ,28      28 , 28
# 4: 17,21       21 , 21
# 5: 22,28       28 , 28
# 6: 17,23       23 , 23
# 7: 22,21       21 , 21
# 8: 25,30       30 , 30
# 9: 20,21       21 , 21

###


###
# El a5eera please

# 1: 3, 8
# 2: 22, 19
# 3: 13, 17 done
# 4: 11, 10 lesa
# 5: 18, 16
# 6: 30, 27
# 7: 16, 16
# 8: 63, 65
# 9: 34, 31
###


###
# Number 1: h: 5, v: 1
# Number 2: h: 9, v: 6
# Number 3: h: 8, v: 5
# Number 4: h: 8, v: 9
# Number 5: h: 12, v: 7
# Number 6: h: 11, v: 8
# Number 7: h: 6, v: 6
# Number 8: h: 11, v: 6
# Number 9: h: 9, v: 6 
###


# 1: 11, 15
# 3: 16, 19
# 4: 18, 21
# 5: 21, 24
# 6: 22, 24
# 7: 12, 18
# 8: 23, 25
# 9: 16, 19
# 2: 15, 17

