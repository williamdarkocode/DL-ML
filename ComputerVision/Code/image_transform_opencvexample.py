import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")

ap.add_argument("-t", "--transformation", required=True, nargs='+', choices=('translate', 'rotate', 'resize'), 
help="One of: 'translate', 'rotate', 'resize'")

ap.add_argument("-x", "--shift_x", required=False, nargs=1, 
help="The number of pixels to shift on the x axis. Negative values for left, positive for right.")

ap.add_argument("-y", "--shift_y", required=False, nargs=1,
help="The number of pixels to shift on the y axis. Negative values for up, positive for down.")

ap.add_argument("-a", "--angle", required=False, nargs=1, help="Angle to rotate the image")
ap.add_argument("-c", "--centre", required=False, nargs=1, help="Centre of rotation, or point around which to rotate image.")

ap.add_argument("-hr", "--height_ratio", required=False, nargs=1, help="Ratio of previous height to new height")
ap.add_argument("-wr", "--width_ratio", required=False, nargs=1, help="Ratio of old width to new width")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
transformation = args["transformation"]

print("Image path: {}, and applied transformation: {}".format(args["image"], transformation))

cv2.imshow("Initial image", image)

def switch(t):
    if t == "translate":
        x = 50 if not args["shift_x"] else int(args["shift_x"][0])
        y = 50 if not args["shift_y"] else int(args["shift_y"][0])
        shifted = imutils.translate(image, x, y)
        cv2.imshow("Translated image x by {}, and y by {}".format(x,y),shifted)
    if t == "rotate":
        a = 90 if not args["angle"] else int(args["angle"][0])
        c = None if not args["centre"] else tuple(args["centre"])
        rotated = imutils.rotate(image, a, center=c, scale=1.0)
        cv2.imshow("Rotated image by {} degree, around {}, and scaled {}".format(a,c,1.0), rotated)
    if t == "resize":
        hr = 
    cv2.waitKey(0)
    


def transform():
    for t in transformation:
        switch(t)


def main():
    transform()

if __name__ == "__main__":
    main()
