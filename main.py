import cv2 as cv
import numpy as np
import os
from time import time
import win32gui, win32con, win32ui

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def window_capture():
    w = 1280 # set this
    h = 800 # set this
    bmpfilenamename = "out.bmp" #set this

    hwnd = win32gui.FindWindow(None, 'HoloCure')
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    
    
    # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    
    return img

loop_time = time()
while True :
    screenshot = window_capture()
 
    cv.imshow('Computer vision', screenshot)
   
    print("FPS : {}".format( 1 / (time() - loop_time)))
    loop_time = time()
        
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllwindowns()
        break


print('done')