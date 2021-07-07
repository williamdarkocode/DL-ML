from typing import Tuple, final
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")

ap.add_argument("-t", "--transformation", required=True, nargs='+', choices=('translate', 'rotate', 'resize', 'flip', 'crop'), 
help="One of: 'translate', 'rotate', 'resize', 'flip', 'crop' ")

ap.add_argument("-x", "--shift_x", required=False, nargs=1, 
help="The number of pixels to shift on the x axis. Negative values for left, positive for right.")

ap.add_argument("-y", "--shift_y", required=False, nargs=1,
help="The number of pixels to shift on the y axis. Negative values for up, positive for down.")

ap.add_argument("-a", "--angle", required=False, nargs=1, help="Angle to rotate the image")
ap.add_argument("-c", "--centre", required=False, nargs=1, help="Centre of rotation, or point around which to rotate image.")

ap.add_argument("-hr", "--height_ratio", required=False, nargs=1, help="Ratio of new height to old height")
ap.add_argument("-wr", "--width_ratio", required=False, nargs=1, help="Ratio of new width to old width")

ap.add_argument("-fd", "--flip_direction", required=False, nargs=1, choices=('0','1','-1'), help="Integer for direction to flip")

ap.add_argument("-ca", "--crop_area", required=False, nargs=1, choices=('cr', 'tl', 'tr', 'bl', 'br'), 
help="One of the following: cr, tl, tr, bl, br, for centre, top-left, top-right, bottom-left, bottom-right, respectively.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
transformation = args["transformation"]
final_image = image
text = ""

print("Image path: {}, and applied transformation: {}".format(args["image"], transformation))

cv2.imshow("Initial image {} height, {} width".format(image.shape[0], image.shape[1]), image)

def switch(t):
    global text
    global final_image
    if t == "translate":
        x = 50 if not args["shift_x"] else int(args["shift_x"][0])
        y = 50 if not args["shift_y"] else int(args["shift_y"][0])
        final_image = imutils.translate(final_image, x, y)
        # cv2.imshow("translated x {} px, y {} px".format(x,y), final_image)
        text += "translated x {} px, y {} px \n ".format(x,y)
    if t == "rotate":
        a = 90 if not args["angle"] else int(args["angle"][0])
        c = None if not args["centre"] else tuple(args["centre"])
        final_image = imutils.rotate(final_image, a, center=c, scale=1.0)
        # cv2.imshow("rotated {} degrees, around {}, scaled {}".format(a,c,1.0), final_image)
        text += "rotated {} degrees, around {}, scaled {} \n ".format(a,c,1.0)
    if t == "resize":
        hr = float(args["height_ratio"][0])
        wr = float(args["width_ratio"][0])
        (oh, ow) = final_image.shape[:2]
        nh = int(hr*oh)
        nw = int(wr*ow)
        final_image = imutils.resize(final_image, width=nw, height=nh)
        # cv2.imshow("resized {} px height, {} px width".format(nh, nw), final_image)
        text += "resized {} px height, {} px width ".format(nh, nw)
    if t == "flip":
        d = int(args["flip_direction"][0])
        sfd = "horizontally" if d == 1 else "vertically"
        sfd = "both horizontally, and vertically" if d == -1 else sfd
        final_image = cv2.flip(final_image, d)
        text+= "flipped {}".format(sfd)
    if t == "crop":
        crop_area = args["crop_area"][0]
        final_image = image[0:int(image.shape[0]/2),0:int(image.shape[1]/2)] if crop_area == "tl" else final_image
        final_image = image[:-int(image.shape[0]/2),-int(image.shape[1]/2):] if crop_area == "tr" else final_image
        final_image = image[-int(image.shape[0]/2):,:-int(image.shape[1]/2)] if crop_area == "bl" else final_image
        final_image = image[-int(image.shape[0]/2):,-int(image.shape[1]/2):] if crop_area == "br" else final_image
        final_image = image[int(image.shape[0]/4):-int(image.shape[0]/4),int(image.shape[1]/4):-int(image.shape[1]/4)] if crop_area == "cr" else final_image
        text+= "cropped area: {}".format(crop_area)

def transform():
    # print("Image shape: {} ".format(image.shape))
    for t in transformation:
        switch(t)
    cv2.putText(final_image, text, (10,20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.4, color=(255,0,0), thickness=1)
    cv2.imshow("Transformed image", final_image)
    cv2.waitKey(0)


def main():
    transform()

if __name__ == "__main__":
    main()
# new directory