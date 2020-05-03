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

# TODO: remove this line - waits until a key is pressed
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()

