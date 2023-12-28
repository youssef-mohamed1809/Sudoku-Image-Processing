import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


def center_image(img1):
    #Image Centering

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
    img1 = cv2.threshold(img1, 110, 255, cv2.THRESH_BINARY)
    img1 = center_image(img1[1])

    x = img1.shape[0]
    y = img1.shape[1]

    ## To draw horizontal lines

    horizotal_lines = np.zeros_like(img1, dtype = np.uint8)

    horizotal_lines = cv2.line(horizotal_lines, (0, 28), (x, 28), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 37), (x, 37), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 42), (x, 42), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 48), (x, 48), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 55), (x, 55), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 62), (x, 62), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 69), (x, 69), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 75), (x, 75), (255, 255, 255), 1)
    horizotal_lines = cv2.line(horizotal_lines, (0, 82), (x, 82), (255, 255, 255), 1)

    ## To draw vertical lines

    vertical_lines = np.zeros_like(img1, dtype = np.uint8)

    vertical_lines = cv2.line(vertical_lines, (28, 0), (28, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (37, 0), (37, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (42, 0), (42, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (48, 0), (48, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (55, 0), (55, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (62, 0), (62, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (69, 0), (69, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (75, 0), (75, y), (255, 255, 255), 1)
    vertical_lines = cv2.line(vertical_lines, (82, 0), (82, y), (255, 255, 255), 1)


    ## Get Intersection points
    horizontal_intersections = horizotal_lines & img1
    vertical_intersections = vertical_lines & img1

    horizontal_count = 0
    vertical_count = 0

    new_img = horizotal_lines + vertical_lines + img1
    plt.imshow(new_img, cmap='gray')
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if horizontal_intersections[i][j] > 230:
                horizontal_count += 1
            if vertical_intersections[i][j] > 230:
                vertical_count += 1
    return horizontal_count, vertical_count

current_num = 9

num1h, num1v = calculate_intersections(f"NumberData/Number{current_num}/num1.jpg")
num2h, num2v = calculate_intersections(f"NumberData/Number{current_num}/num2.jpg")
num3h, num3v = calculate_intersections(f"NumberData/Number{current_num}/num3.jpg")
num4h, num4v = calculate_intersections(f"NumberData/Number{current_num}/num4.jpg")
num5h, num5v = calculate_intersections(f"NumberData/Number{current_num}/num5.jpg")
num6h, num6v = calculate_intersections(f"NumberData/Number{current_num}/num6.jpg")
num9h, num9v = calculate_intersections(f"NumberData/Number{current_num}/num9.jpg")
num10h, num10v = calculate_intersections(f"NumberData/Number{current_num}/num10.jpg")
num11h, num11v = calculate_intersections(f"NumberData/Number{current_num}/num11.jpg")
num14h, num14v = calculate_intersections(f"NumberData/Number{current_num}/num14.jpg")

total_horizontal = num1h + num2h + num3h + num4h + num5h + num6h + num9h + num10h + num11h + num14h
total_vertical = num1v + num2v + num3v + num4v + num5v + num6v + num9v + num10v + num11v + num14v

avg_horizontal = total_horizontal // 10
avg_vertical = total_vertical // 10
print(f"Average Horizontal Lines: {avg_horizontal}")
print(f"Average Vertical Lines: {avg_vertical}")


###

# 1: 23, 16
# 2: 43, 39
# 3: 40, 45
# 4: 35, 36
# 5: 39, 38
# 6: 38, 45
# 7: 24, 28
# 8: 51, 44
# 9: 

###