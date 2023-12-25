import cv2
import matplotlib.pyplot as plt
import numpy as np
import math





img1 = cv2.imread('NumberData/Number3/num14.jpg')
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
print(f"X: {x}, Y: {y}")
print(l1Start)
print(l2Start)
print(l3Start)

image = np.zeros_like(img1, dtype = np.uint8)

image = cv2.line(image, (0, 18), (x, 18), (255, 255, 255), 1)
image = cv2.line(image, (0, 35), (x, 35), (255, 255, 255), 1)
image = cv2.line(image, (0, 53), (x, 53), (255, 255, 255), 1)
image = cv2.line(image, (0, 72), (x, 72), (255, 255, 255), 1)
image = cv2.line(image, (0, 90), (x, 90), (255, 255, 255), 1)
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
print("vertical")
print(l1vStart)
print(l2vStart)
print(l3vStart)

image = cv2.line(image, (18, 0), (18, y), (255, 255, 255), 1)
image = cv2.line(image, (35, 0), (35, y), (255, 255, 255), 1)
image = cv2.line(image, (53, 0), (53, y), (255, 255, 255), 1)
image = cv2.line(image, (72, 0), (72, y), (255, 255, 255), 1)
image = cv2.line(image, (90, 0), (90, y), (255, 255, 255), 1)
image = cv2.line(image, (108, 0), (108, y), (255, 255, 255), 1)


## Get Intersection points
intersectionPoints = img1 & image

# print(img1.shape)
count = 0

for i in range(intersectionPoints.shape[0]):
    for j in range(intersectionPoints.shape[1]):
        if intersectionPoints[i][j] > 250:

            count += 1


print(count)