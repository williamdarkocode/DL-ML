import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-d", "--dest", required=True, help="Destination of the final image; provide relative path.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#show the initial image
cv2.imshow("My cool image", image)

# opencv stores pixels as tuples of rgb, but open cv stores them backwards as bgr. a single pixel is stored as (b, g, r)
(b,g,r) = image[0,0] #selects the first pixel (upper leftmost pixel. pixel couting starts from upper left corner)
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

#set the upper left most pixel to all red
image[0,0] = (0, 0, 255)

(b,g,r) = image[0,0] #selects the first pixel (upper leftmost pixel. pixel couting starts from upper left corner)
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

print(image.shape)

# set the entire bottom right 500 x 500 corner to red pixels
b_r_corner = image[-500:,-500:]
cv2.imshow("br_corner", b_r_corner)

image[-500:,-500:] = (0,0,255)

b_r_corner = image[-500:,-500:] #100 x 100 bottom right corner of the image

# numpy syntax for accessing pixels (2d arrays/matrices) is mat[y,x] or mat[row, col]

cv2.imshow("br_corner", b_r_corner)

cv2.imshow("edited image", image)



cv2.waitKey(0)