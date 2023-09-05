import cv2 as cv
import numpy as np
import win32gui
from windownCapture import window_capture as wc

# wincap = wc('Aether Gazer')

# while True :
#     screenshot = wincap.get_capture()
    
#     cv.imshow('Computer vision', screenshot)
        
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllwindowns()
#         break
    
    
'''List of windows'''
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )

win32gui.EnumWindows( winEnumHandler, None )
winEnumHandler()