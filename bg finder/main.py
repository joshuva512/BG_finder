import numpy as np
import cv2
from skimage import data, filters
from tkinter import Tk
from tkinter.filedialog import askopenfilename



Tk().withdraw()
filelocation = askopenfilename()
try:
    cap = cv2.VideoCapture(filelocation)
    framesid = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
    frame = []
    for fid in framesid:
         cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
         _, fm = cap.read()
         frame.append(fm)
    
    me = np.median(frame, axis=0).astype(dtype=np.uint8)
    cv2.imshow('pic', me)
    cv2.waitKey(0)
except:
    print("select video file")
