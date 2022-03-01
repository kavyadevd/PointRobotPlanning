import imp
import pygame
import numpy as np
from Obstacle import Obstacle

# define variables
bot_clearance = 5

# scaling factor for better visualization
zoom_ = 1

# create pygame environment
screen_size = width, height = 400*zoom_, 250*zoom_
screen = pygame.display.set_mode(screen_size)
black = [0, 0, 0]
white = [255, 255, 255]
screen.fill(white)

polygon1_points = [[115, 210], [80, 180], [105, 100], [36, 185]]

# Get and validate user input
start_pos = [68, 178]
goal_pos = [335, 185]


def draw_map():
    pygame.init()
    # circle(surface, color, center, radius)
    pygame.draw.circle(screen, black, (300, (250-185)), 40)
    # polygon(surface, color, points)
    pygame.draw.polygon(screen, black, polygon1_points, True)
    # Hexagon02
    pygame.display.flip()


def StartDijkstra():
    draw_map()
    pygame.time.wait(5000)


# Create Obstacles
obstacles_ = Obstacle(bot_clearance, start_pos, height, width,polygon1_points)
obstacles_.AddObstacle("circle", [[300, 185], [40]])
obstacles_.AddObstacle(
    "polygon", [[115, 210], [75, 180], [105, 100], [36, 186]])
obstacles_.AddObstacle("hexagon", [])
flag = obstacles_.ValidateAll(start_pos)
if flag:
    flag = obstacles_.ValidateAll(goal_pos, obstacles_)
if flag:
    StartDijkstra()
