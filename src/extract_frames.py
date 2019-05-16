import sys
import os.path
import numpy as np
import cv2 as cv

if (len(sys.argv) != 3):
    print('---Invalid number of command line arguments passed---')
    print('It should be as follows:')
    print('python extract_frames.py video_name directory_name')
    print('video_name => name of the video that will have the extracted frames')
    print('directory_name => directory where the frames will be saved. If the directory does not exist, a new one will be created')
    sys.exit()


directory_path = './assets/' + sys.argv[2]

if not os.path.exists(directory_path):
    os.makedirs(directory_path)