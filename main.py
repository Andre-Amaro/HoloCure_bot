import cv2 as cv
import numpy as np

game_shot = cv.imread("map3/sprits/map.png",cv.IMREAD_UNCHANGED)
enemy1 = cv.imread("map3/sprits/enemy1.png",cv.IMREAD_UNCHANGED)
enemy2= cv.imread("map3/sprits/enemy2.png",cv.IMREAD_UNCHANGED)

enemy1_result = cv.matchTemplate(game_shot,enemy1, cv.TM_CCOEFF_NORMED)
enemy2_result = cv.matchTemplate(game_shot,enemy2, cv.TM_CCOEFF_NORMED)


'''Best location for the matches'''
min_val_enemy1, max_val_enemy1, min_loc_enemy1, max_loc_enemy1 = cv.minMaxLoc(enemy1_result)

'''enemy 1 where are u'''
threshold_enemy1 = 0.53
locations_enemy1 = np.where(enemy1_result >= threshold_enemy1)
locations_enemy1 = list(zip(*locations_enemy1[::-1]))
'''enemy 2 where are u'''
threshold_enemy2 = 0.52
locations_enemy2 = np.where(enemy2_result >= threshold_enemy2)
locations_enemy2 = list(zip(*locations_enemy2[::-1]))

'''DEBUGG'''
# cv.imshow('Result', result)
# cv.waitKey()
# print(f'Best match top left position  {str(max_loc)}')
# print(f'Best Match confidence : {max_val}')

if locations_enemy1:
    print("Found enemy")
    
    enemy1_w = enemy1.shape[1]
    enemy1_h = enemy1.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4
    
    #Draw locations 
    for loc in locations_enemy1:
        
        top_left = loc
        bottom_right = (top_left[0] + enemy1_w, top_left[1] + enemy1_h )
        
        cv.rectangle(game_shot, top_left, bottom_right, line_color, line_type)
        
    # cv.imshow('Matches results', game_shot)
    # cv.waitKey()
else:
    print('Not found')
    
if locations_enemy2:
    print("Found enemy")
    
    enemy2_w = enemy2.shape[1]
    enemy2_h = enemy2.shape[0]
    line_color = (255,0,0)
    line_type = cv.LINE_4
    
    #Draw locations 
    for loc in locations_enemy2:
        
        top_left = loc
        bottom_right = (top_left[0] + enemy2_w, top_left[1] + enemy2_h )
        
        cv.rectangle(game_shot, top_left, bottom_right, line_color, line_type)
        
    # cv.imshow('Matches results', game_shot)
    # cv.waitKey()
else:
    print('Not found')
    
cv.imshow('Matches Results', game_shot)
cv.waitKey()