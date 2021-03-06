### This script is just for image collection. For full data information use the "input.py" script ###


import os
import numpy as np
import cv2 as opencv
import time
from track_view import image_processing
from PIL import ImageGrab
from test_keys import pressed_released_key


# Change path
path = os.getcwd()

# Input Size
width = 1050
height = 900

# Recording frames with delta
i_frame = 0

# Recording to current folder
while(True):
    i_frame += 1
    screen_recording = ImageGrab.grab(bbox=(0, 0, width, height))
    screenArray = np.array(screen_recording)
    frameConversion = opencv.cvtColor(screenArray, opencv.COLOR_BGR2RGB)

    edges = image_processing(frameConversion)

    lines = opencv.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            lines = opencv.line(frameConversion, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Recording frames
    opencv.imwrite(os.path.join(path, 'Image_' + str(i_frame) + '.jpg'), frameConversion)

    if opencv.waitKey(1) == ord('t'):
        opencv.destroyAllWindows()
        break