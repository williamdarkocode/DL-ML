import argparse
import imutils
import cv2

# create cmd line argument parser and specify arguments it'll take
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", "--i", required=True, help="Provide the path the input image")
ap.add_argument("-o", "--output", required=True, help="Provide the path to the file output will be written to")
args = vars(ap.parse_args())

img = cv2.imread(args["input"])

# grayscale, blur, and threshold the image
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayscale, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in image and extract
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# iterate over contours and draw them on the input image
for contour in contours:
    cv2.drawContours(img, [contour], -1, (0,0,255), 2)

#display the total number of shapes on the image
text = "Found {} total shapes".format(len(contours))
cv2.putText(img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

# write the resulting image to disk at the provided output path, and show the image
cv2.imwrite(args["output"], img)

result_img = cv2.imread(args["output"])
cv2.imshow("Shape count: ", result_img)
cv2.waitKey(0)

# conda update:
# conda update -n base -c defaults conda
#  new directory