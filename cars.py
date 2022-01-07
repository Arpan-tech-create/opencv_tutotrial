import cv2

import matplotlib.pyplot as plt

import cvlib as cv
from cvlib.object_detection import draw_bbox

im=cv2.imread("C:\Users\ARPAN\Downloads\group_of_cars_thumb800.jpg")

bbox,label,conf