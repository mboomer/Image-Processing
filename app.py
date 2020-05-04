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

# read in image and make a grayscale copy
color_original = cv2.imread('test.jpg')
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)

# this was needed before filters were added to avoid an undef error later
# colour image to be modified
# color_modified = color_original
# grayscale image to be modified
# gray_modified = gray_original

# define convolution kernels
# how the calc works for box_kernal
# (1 + 2 + 3 + 4 + 5) / 5 
# is the same as doing  
# 1 * 1/5 + 2 * 1/5 + 3 * 1/5 + 4 * 1/5 + 5 * 1/5
identity_kernel  = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
sharpen_kernel   = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
gaussian_kernel1 = cv2.getGaussianKernel(3, 0)    # defines a 3x3 array for the sliding window
gaussian_kernel2 = cv2.getGaussianKernel(5, 0)    # defines a 5x5 array for the sliding window
box_kernel       = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32) / 9.0
kernels = [identity_kernel, sharpen_kernel, gaussian_kernel1, gaussian_kernel2, box_kernel]

# create UI window
cv2.namedWindow('app')

# args name, window, initial value, max value, onChange event handler
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy)           # if new kernals (filters) are added this will still work
cv2.createTrackbar('greyscale', 'app', 0, 1, dummy)                     # greyscale is a switch on/of

# create counter for use with the file name
count = 1
    
# create UI loop
while True:
    # read all trackbar values
    contrast   = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    kernel_idx = cv2.getTrackbarPos('filter', 'app')                    # filter trackbar is the index to kernel array
    grayscale  = cv2.getTrackbarPos('greyscale', 'app')

    # apply filters
    color_modified = cv2.filter2D(color_original, -1, kernels[kernel_idx])
    gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel_idx])

    # apply the brightness and contrast
    # use np to create an array thats the same size as the original image
    # brightness starts at 50, this allows the brightness to be reduced as well as increased
    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_original), 0, brightness - 50)
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_original), 0, brightness - 50)

    # wait for a key to be pressed for 200 millisecs
    # key is the ordinal value of the key pressed
    # q=quit s=save
    key = cv2.waitKey(200)
    if key == ord('q'):
        break
    elif key == ord('s'):
        if grayscale == 0:
            cv2.imwrite ('output-{}.png'.format(count), color_modified)
        else:
            cv2.imwrite('output-{}.png'.format(count), gray_modified)
        count += 1
        
    # display the image in the app window
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

# destroy all windows
cv2.destroyAllWindows()
