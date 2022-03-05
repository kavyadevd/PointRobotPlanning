#import pygame
import numpy as np
from Obstacle import Obstacle
from Obstacle import Game
import matplotlib.pyplot as plot
from pygame.locals import *
import cv2

# define variables
bot_clearance = 5

# create pygame environment
screen_size = width, height = 400, 250
image = np.zeros((height, width, 3), np.uint8)
image.fill(255)
#screen = pygame.display.set_mode(screen_size)
black = [0, 0, 0]
white = [255, 255, 255]
poly_color = [195,89,143]
blue = [0, 0, 255]
border_c = [64, 106, 151]
# screen.fill(white)

polygon1_points = [[115, 210], [80, 180], [105, 100], [36, 185]]
polygon2_points = [[200, 140], [235, 120], [
    235, 80], [200, 60], [165, 80], [165, 120]]

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

# fig1, axes = plot.subplots()


def DrawMap(points, path):
    global image
    image = cv2.flip(image, 0)
    image = cv2.flip(image, 1)
    nppolygon1_points = np.array(polygon1_points,np.int32)
    nppolygon1_points = nppolygon1_points.reshape(-1,1,2)
    image = cv2.fillPoly(image, [nppolygon1_points], poly_color)

    # Plot start goal points
    image[start_pos[0], start_pos[1]] = [0, 0, 255]

    cv2.putText(image, 'Start', (start_pos[0], start_pos[1]),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
    image[goal_pos[0], goal_pos[1]] = [0, 0, 255]
    cv2.putText(image, 'Goal', (goal_pos[0], goal_pos[1]),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)

    # Circle
    image = cv2.circle(image, (300, 185), 40, poly_color, -1)

    # Hexagon
    nppolygon1_points = np.array(polygon2_points,np.int32)
    image = cv2.fillPoly(image, [nppolygon1_points], poly_color)

    # Clearance
    nppolygon1_points = np.array(poly1_offset,np.int32)
    image = cv2.polylines(image, [nppolygon1_points], True, border_c, 1)

    nppolygon1_points = np.array(hexa_offset,np.int32)
    image = cv2.polylines(image, [nppolygon1_points], True, border_c, 1)


    image = cv2.circle(image, (300, 185), 45, border_c, 1)

    # Animate Dijkstra space
    # Plot point space : EXPLORED
    image_ =image
    for vis in points:
        image_[int(vis[1]), int(vis[0]), :] = [121,166,77]
        img = image_.copy()
        img = cv2.flip(image, -1)
        img = cv2.flip(image, 0)
        cv2.imshow("Moving", img)
        cv2.waitKey(1)
    cv2.waitKey(0)

    # Plot PATH
    for p in path:
        image = cv2.circle(image, (int(p[0]), int(p[1])), 2, blue, 1)
    


# Create Obstacles
obstacles_ = Obstacle(bot_clearance, start_pos, height,
                      width, polygon1_points, polygon2_points)
obstacles_.AddObstacle("circle", [[300, 185], [40]])
obstacles_.AddObstacle("polygon", polygon1_points)
obstacles_.AddObstacle("hexagon", polygon2_points)
flag = obstacles_.ValidateAll(start_pos)


def StartGame(start_pos, goal_pos, bot_clearance):
    global obstacles_
    game_ = Game(start_pos, goal_pos, bot_clearance, obstacles_)
    path, points = game_.Start()
    DrawMap(points, path)
    plot.show()
    # pygame.time.wait(5000)


if flag:
    flag = obstacles_.ValidateAll(goal_pos)
else:
    print('Invalid start position')
if flag:
    global poly1_offset
    poly1_offset = obstacles_.polygon_with_border
    global hexa_offset
    hexa_offset = obstacles_.hexagon_with_border
    StartGame(start_pos, goal_pos, bot_clearance)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image = cv2.flip(image, -1)
    image = cv2.flip(image, 0)
    cv2.imshow('Path', image)
    cv2.waitKey(0)
    cv2.imwrite("Output.png", image)
    # pygame.quit()
    exit()
else:
    print('Invalid goal position')
