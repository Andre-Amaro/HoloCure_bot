import cv2 as cv
import numpy as np

game_shot = cv.imread("map3/sprits/map.png",cv.IMREAD_UNCHANGED)
enemy1 = cv.imread("map3/sprits/enemy1.png",cv.IMREAD_UNCHANGED)
enemy2= cv.imread("map3/sprits/enemy2.png",cv.IMREAD_UNCHANGED)
bat_enemy = cv.imread("map3/sprits/bat.png",cv.IMREAD_UNCHANGED)

enemy1_w = enemy1.shape[1]
enemy1_h = enemy1.shape[0]
enemy2_w = enemy2.shape[1]
enemy2_h = enemy2.shape[0]
bat_w = bat_enemy.shape[1]
bat_h = bat_enemy.shape[0]



enemy1_result = cv.matchTemplate(game_shot,enemy1, cv.TM_CCOEFF_NORMED)
enemy2_result = cv.matchTemplate(game_shot,enemy2, cv.TM_CCOEFF_NORMED)
bat_result = cv.matchTemplate(game_shot,bat_enemy, cv.TM_SQDIFF_NORMED)



'''Best location for the matches'''
# min_val_enemy1, max_val_enemy1, min_loc_enemy1, max_loc_enemy1 = cv.minMaxLoc(enemy1_result)

'''enemy 1 where are u'''
threshold_enemy1 = 0.56
locations_enemy1 = np.where(enemy1_result >= threshold_enemy1)
locations_enemy1 = list(zip(*locations_enemy1[::-1]))
'''enemy 2 where are u'''
threshold_enemy2 = 0.56
locations_enemy2 = np.where(enemy2_result >= threshold_enemy2)
locations_enemy2 = list(zip(*locations_enemy2[::-1]))
'''enemy 2 type 2 where are u'''
threshold_bat = 0.20
locations_bat = np.where(bat_result <= threshold_bat)
locations_bat = list(zip(*locations_bat[::-1]))

'''Merger rectangles'''
rectangles_enemy1 = []
rectangles_enemy2 = []
rectangles_bat = []


for rect_1 in locations_enemy1:
    rect_enemy1 = [int(rect_1[0]), int(rect_1[1]), enemy1_w, enemy1_h]
    rectangles_enemy1.append(rect_enemy1)
    rectangles_enemy1.append(rect_enemy1)
    
for rect_2 in locations_enemy2:
    rect_enemy2 = [int(rect_2[0]), int(rect_2[1]), enemy2_w, enemy2_h]
    rectangles_enemy2.append(rect_enemy2)
    rectangles_enemy2.append(rect_enemy2)
    
for rect_bat_ in locations_bat:
    rect_bat = [int(rect_bat_[0]), int(rect_bat_[1]), bat_w, bat_h]
    rectangles_bat.append(rect_bat)
    rectangles_bat.append(rect_bat)

rectangles_enemy1, weight = cv.groupRectangles(rectangles_enemy1, 1, 0.5)
rectangles_enemy2, weight = cv.groupRectangles(rectangles_enemy2, 1, 0.05)
rectangles_bat, weight = cv.groupRectangles(rectangles_bat, 1, 0.5)


'''DEBUGG'''
# cv.imshow('Result', result)
# cv.waitKey()
# print(f'Best match top left position  {str(max_loc)}')
# print(f'Best Match confidence : {max_val}')

if len(rectangles_enemy1):
    print("Found enemy")
    

    line_color = (0,255,0)
    line_type = cv.LINE_4
    
    #Draw locations 
    for (x,y,w,h) in rectangles_enemy1:
        
        top_left = (x,y)
        bottom_right = (x + w , y + h)
        
        cv.rectangle(game_shot, top_left, bottom_right, line_color, line_type)
        

else:
    print('Not found')
    
if len(rectangles_enemy2):
    print("Found enemy")
    
    line_color = (255,0,0)
    line_type = cv.LINE_4
    
    #Draw locations 
    for (x,y,w,h) in rectangles_enemy2:
        
        top_left = (x,y)
        bottom_right = (x + w, y + h)
        
        cv.rectangle(game_shot, top_left, bottom_right, line_color, line_type)

else:
    print('Not found')
if len(rectangles_bat):
    print("Found enemy")
    
    line_color = (255,0,0)
    line_type = cv.LINE_4
    
    #Draw locations 
    for (x,y,w,h) in rectangles_bat:
        
        top_left = (x,y)
        bottom_right = (x + w, y + h)
        
        cv.rectangle(game_shot, top_left, bottom_right, line_color, line_type)
        

else:
    print('Not found')
    
cv.imshow('Matches Results', game_shot)
cv.waitKey()