# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:09:53 2020

@author: Mark Boomer
"""
import cv2 as cv2
import numpy as np

# dummy function that does nothing at present
def dummy(value):
    pass

# create UI window and track bars
cv2.namedWindow('app')

color_original = cv2.imread('test.jpg')
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)

# colour image to be modified
color_modified = color_original
# grayscale image to be modified
gray_modified = gray_original

# args name, window, initial value, max value, onChange event handler
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
# TODO: update the number of filters
cv2.createTrackbar('filters', 'app', 0, 1, dummy)
# greyscale is a switch on/of
cv2.createTrackbar('greyscale', 'app', 0, 1, dummy)

# create UI loop
while True:
    # TODO: read all trackbar values
    contrast   = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    filters    = cv2.getTrackbarPos('filters', 'app')
    grayscale  = cv2.getTrackbarPos('greyscale', 'app')

    # apply the brightness and contrast
    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_original), 0, brightness - 50)
    gray_modified  = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_original), 0, brightness - 50)

    # TODO: apply filters
    # TODO: apply brightness and contrast
    # TODO: apply greyscale
    
    # wait for a key to be pressed for 200 millisecs
    key = cv2.waitKey(200)
    # key is the ordinal value of the key pressed
    if key == ord('q'):
        break
    elif key == ('s'):
        # TODO: save the image
        pass

    # display the image in the app window
    if grayscale == 0:
        # TODO: replace with final modified image
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

# destroy all windows
cv2.destroyAllWindows()

