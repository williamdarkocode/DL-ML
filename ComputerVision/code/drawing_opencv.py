import math
import numpy as np
import cv2

canvas = np.zeros((1000,1000, 3), dtype="uint8") # shape (height, width, colour channels)

# remember opencv uses rgb but backwards: (b, g, r), thus (0,0,255) is RED not blue

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

colour_clock = [red, green, blue]

cv2.line(canvas, (0,0),(1000,1000),red)
cv2.line(canvas, (1000,0),(0,1000),red)
cv2.line(canvas,(500,0), (500,1000), green)
cv2.line(canvas, (0,500), (1000,500), blue)

cv2.imshow("initial lines art", canvas)

width = canvas.shape[1]
dim = canvas.shape[1]
colour = 0
canvas[:dim,:dim] = colour_clock[colour]
colour+=1
dim = math.floor(dim/2)
while dim >= 1:
    diff = width - dim
    epsilon_delta = math.floor(diff/2)
    neg_e_d = 0 - epsilon_delta
    print(dim, epsilon_delta, neg_e_d)
    canvas[epsilon_delta:neg_e_d, epsilon_delta:neg_e_d] = colour_clock[colour]
    # cv2.line(canvas, (epsilon_delta, epsilon_delta), (neg_e_d, neg_e_d), colour)
    colour = (colour+1) % 3
    dim = math.floor(dim/2)



cv2.imshow("abstract art", canvas)
cv2.waitKey(0)
#  new dir