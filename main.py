import cv2 as cv
import numpy as np

game_shot = cv.imread("map3/sprits/map.png",cv.IMREAD_UNCHANGED)
enemy1_img = cv.imread("map3/sprits/enemy1.png",cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(game_shot,enemy1_img, cv.TM_CCOEFF_NORMED)

'''Best location for the matches'''
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

threshold = 0.7
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))

print(locations)

'''DEBUGG'''
# cv.imshow('Result', result)
# cv.waitKey()
# print(f'Best match top left position  {str(max_loc)}')
# print(f'Best Match confidence : {max_val}')

# threshold = 0.8
# if max_val >= threshold:
#     print('Found')
    
#     #get dimensions of the enemy
#     enemy1_w = enemy1_img.shape[1]
#     enemy1_h = enemy1_img.shape[0]
    
#     top_left = max_loc
#     bottom_right = (top_left[0] + enemy1_w, top_left[1] + enemy1_h)
    
#     cv.rectangle(game_shot, top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
#     cv.imshow('Result', game_shot)
#     cv.waitKey()
# else :
#     print('Not here')