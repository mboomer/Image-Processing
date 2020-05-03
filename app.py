# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:09:53 2020

@author: Mark Boomer
"""
import cv2 as cv2
import numpy as pd

# dummy function that does nothing at present
def dummy(value):
    pass

# create UI window and track bars
cv2.namedWindow('app')

# args name, window, initial value, max value, onChange event handler
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
# TODO: update the number of filters
cv2.createTrackbar('filters', 'app', 0, 1, dummy)
# greyscale is a switch on/of
cv2.createTrackbar('greyscale', 'app', 0, 1, dummy)

# create UI loop
while True:
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

# destroy all windows
cv2.destroyAllWindows()

