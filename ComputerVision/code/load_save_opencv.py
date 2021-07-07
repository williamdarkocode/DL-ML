import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-d", "--dest", required=True, help="Path to save final image")
args = vars(ap.parse_args())

# read image and display dimensions
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1])) # shape is (height, width) or (rows, columns)
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2])) # colour channels are usually third element in shape tuple... at least in opencv

# display the image
cv2.imshow("My cool image", image)

#write the img to a file
cv2.imwrite(args["dest"], image) # write the image to the value with key "dest" in args
# if destination file doesn't exist at path, imwrite creates it at the given path

cv2.waitKey(0)
#  new dir
