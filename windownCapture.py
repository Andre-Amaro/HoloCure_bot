import cv2 as cv
import numpy as np
import os
from time import time
import win32gui, win32con, win32ui



class window_capture:
    w = 0 # set this
    h = 0 # set this
    hwnd = None
    
    def __init__(self, window_name):
        
        self.hwnd = win32gui.FindWindow(None, 'HoloCure')
               
        window_rect = win32gui.GetWindowRect(self.hwnd)       
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        
        if not self.hwnd:
            raise Exception("Window not found {}".format(window_name))
    
    def get_capture(self):
  

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)
        
        
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        
        
        
        '''removing the alpha channel'''
        img = img[...,:3]
        img = np.ascontiguousarray(img)
        
        return img


