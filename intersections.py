import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_intersections(path):
    img1 = cv2.imread(path)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


    x = img1.shape[0]
    y = img1.shape[1]

    ## To draw horizontal lines
    halfy = y // 2

    l1Start = (0, halfy)
    l1End = (x, halfy)

    quartery = halfy // 2
    l2Start = (0, quartery)
    l2End = (x, quartery)

    l3Start = (0, halfy + quartery)
    l3End = (x, halfy + quartery)

    image = np.zeros_like(img1, dtype = np.uint8)

    image = cv2.line(image, (0, 5), (x, 5), (255, 255, 255), 1)
    image = cv2.line(image, (0, 9), (x, 9), (255, 255, 255), 1)
    image = cv2.line(image, (0, 13), (x, 13), (255, 255, 255), 1)
    image = cv2.line(image, (0, 18), (x, 18), (255, 255, 255), 1)
    image = cv2.line(image, (0, 22), (x, 22), (255, 255, 255), 1)
    image = cv2.line(image, (0, 26), (x, 26), (255, 255, 255), 1)
    image = cv2.line(image, (0, 30), (x, 30), (255, 255, 255), 1)
    image = cv2.line(image, (0, 35), (x, 35), (255, 255, 255), 1)
    image = cv2.line(image, (0, 39), (x, 39), (255, 255, 255), 1)
    image = cv2.line(image, (0, 44), (x, 44), (255, 255, 255), 1)
    image = cv2.line(image, (0, 48), (x, 48), (255, 255, 255), 1)
    image = cv2.line(image, (0, 53), (x, 53), (255, 255, 255), 1)
    image = cv2.line(image, (0, 57), (x, 57), (255, 255, 255), 1)
    image = cv2.line(image, (0, 62), (x, 62), (255, 255, 255), 1)
    image = cv2.line(image, (0, 66), (x, 66), (255, 255, 255), 1)
    image = cv2.line(image, (0, 72), (x, 72), (255, 255, 255), 1)
    image = cv2.line(image, (0, 76), (x, 76), (255, 255, 255), 1)
    image = cv2.line(image, (0, 81), (x, 81), (255, 255, 255), 1)
    image = cv2.line(image, (0, 85), (x, 85), (255, 255, 255), 1)
    image = cv2.line(image, (0, 90), (x, 90), (255, 255, 255), 1)
    image = cv2.line(image, (0, 94), (x, 94), (255, 255, 255), 1)
    image = cv2.line(image, (0, 99), (x,99), (255, 255, 255), 1)
    image = cv2.line(image, (0, 103), (x, 103), (255, 255, 255), 1)
    image = cv2.line(image, (0, 108), (x, 108), (255, 255, 255), 1)

    ## To draw vertical lines
    halfx = x // 2
    l1vStart = (halfx, 0)
    l1vEnd = (halfx, y)

    quarterx = halfx // 2
    l2vStart = (quarterx, 0)
    l2vEnd = (quarterx, y)

    l3vStart = (halfx + quarterx, 0)
    l3vEnd = (halfx + quarterx, y)
 
    image = cv2.line(image, (5, 0), (5, y), (255, 255, 255), 1)
    image = cv2.line(image, (9, 0), (9, y), (255, 255, 255), 1)
    image = cv2.line(image, (13, 0), (13, y), (255, 255, 255), 1)
    image = cv2.line(image, (18, 0), (18, y), (255, 255, 255), 1)
    image = cv2.line(image, (22, 0), (22, y), (255, 255, 255), 1)
    image = cv2.line(image, (26, 0), (26, y), (255, 255, 255), 1)
    image = cv2.line(image, (30, 0), (30, y), (255, 255, 255), 1)
    image = cv2.line(image, (35, 0), (35, y), (255, 255, 255), 1)
    image = cv2.line(image, (39, 0), (39, y), (255, 255, 255), 1)
    image = cv2.line(image, (44, 0), (44, y), (255, 255, 255), 1)
    image = cv2.line(image, (48, 0), (48, y), (255, 255, 255), 1)
    image = cv2.line(image, (53, 0), (53, y), (255, 255, 255), 1)
    image = cv2.line(image, (57, 0), (57, y), (255, 255, 255), 1)
    image = cv2.line(image, (62, 0), (62, y), (255, 255, 255), 1)
    image = cv2.line(image, (66, 0), (66, y), (255, 255, 255), 1)
    image = cv2.line(image, (72, 0), (72, y), (255, 255, 255), 1)
    image = cv2.line(image, (76, 0), (76, y), (255, 255, 255), 1)
    image = cv2.line(image, (81, 0), (81, y), (255, 255, 255), 1)
    image = cv2.line(image, (85, 0), (85, y), (255, 255, 255), 1)
    image = cv2.line(image, (90, 0), (90, y), (255, 255, 255), 1)
    image = cv2.line(image, (94, 0), (94, y), (255, 255, 255), 1)
    image = cv2.line(image, (99, 0), (99, y), (255, 255, 255), 1)
    image = cv2.line(image, (103, 0), (103, y), (255, 255, 255), 1)
    image = cv2.line(image, (108, 0), (108, y), (255, 255, 255), 1)


    ## Get Intersection points
    intersectionPoints = img1 & image
    count = 0

    for i in range(intersectionPoints.shape[0]):
        for j in range(intersectionPoints.shape[1]):
            if intersectionPoints[i][j] > 250:

                count += 1
    return count

current_num = 9

num1 = calculate_intersections(f"NumberData/Number{current_num}/num1.jpg")
num2 = calculate_intersections(f"NumberData/Number{current_num}/num2.jpg")
num4 = calculate_intersections(f"NumberData/Number{current_num}/num4.jpg")
num6 = calculate_intersections(f"NumberData/Number{current_num}/num6.jpg")
num9 = calculate_intersections(f"NumberData/Number{current_num}/num9.jpg")
num11 = calculate_intersections(f"NumberData/Number{current_num}/num11.jpg")
num14 = calculate_intersections(f"NumberData/Number{current_num}/num14.jpg")

total = num1 + num2 + num4 + num6  + num9 + num11 + num14

avg = total // 7
print(avg)

###
# 1: 61
# 2: 84
# 3: 96
# 4: 81
# 5: 103
# 6: 102
# 7: 73
# 8: 115
# 9: 95
###

###
# 1: 31
# 2: 47
# 3: 50
# 4: 43
# 5: 51
# 6: 52
# 7: 41
# 8: 60
# 9: 54
###

###
# 1: 12
# 2: 24
# 3: 25
# 4: 25
# 5: 24
# 6: 26
# 7: 21
# 8: 29
# 9: 25
###