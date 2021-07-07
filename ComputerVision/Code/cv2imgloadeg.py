import cv2

print(cv2.__version__)

image = cv2.imread("./images/blackhole.jpeg")

print(image.shape)

cv2.imshow("Image", image)
cv2.waitKey(0)
#  new directory
