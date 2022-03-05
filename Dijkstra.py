#import pygame
import numpy as np
from Obstacle import Obstacle
from Obstacle import Game
import matplotlib.pyplot as plot
from matplotlib import animation

# define variables
bot_clearance = 5

# create pygame environment
screen_size = width, height = 400, 250
#screen = pygame.display.set_mode(screen_size)
black = [0, 0, 0]
white = [255, 255, 255]
red = [255,0,0]
blue = [0,0,255]
#screen.fill(white)

polygon1_points = [[115, 210], [80, 180], [105, 100], [36, 185]]
polygon2_points = [[200, 140], [235,120], [235,80], [200,60],[165,80],[165,120]]

# Get and validate user input
print('Input start position')
start_pos = []
temp = input('x:')
start_pos.append(int(temp))
temp = input('y:')
start_pos.append(int(temp))
if not start_pos:
    start_pos = [68, 178]
print('Input goal position')
goal_pos = []
temp = input('x:')
goal_pos.append(int(temp))
temp = input('y:')
goal_pos.append(int(temp))
if not goal_pos:
    goal_pos = [335, 185]

fig1, axes = plot.subplots()

# Create Obstacles
obstacles_ = Obstacle(bot_clearance, start_pos, height, width,polygon1_points, polygon2_points)
obstacles_.AddObstacle("circle", [[300, 185], [40]])
obstacles_.AddObstacle("polygon", polygon1_points)
obstacles_.AddObstacle("hexagon", polygon2_points)
flag = obstacles_.ValidateAll(start_pos)


def StartGame(start_pos,goal_pos,bot_clearance):
    global obstacles_
    game_ = Game(start_pos, goal_pos, bot_clearance, obstacles_)
    path, points = game_.Start()
 
    plot.show()
    #pygame.time.wait(5000)


if flag:
    flag = obstacles_.ValidateAll(goal_pos)
if flag:
    global poly1_offset
    poly1_offset = obstacles_.polygon_with_border
    global hexa_offset
    hexa_offset = obstacles_.hexagon_with_border
    StartGame(start_pos,goal_pos,bot_clearance)
    #pygame.quit()
    exit()






