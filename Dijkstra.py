import pygame
import numpy as np


bot_clearance = 5

pygame.init()
screen_size = width, height = 400, 250
screen = pygame.display.set_mode(screen_size)
black = [0, 0, 0]
white = [255, 255, 255]
screen.fill(white)


def validate(pos):
    if bot_clearance <= pos[0] >= (width-bot_clearance) or bot_clearance <= pos[1] >= (height-bot_clearance):
        print('Entered ponit is not within map dimensions')


def draw_map():
    # circle(surface, color, center, radius)
    pygame.draw.circle(screen, black, (300, (250-185)), 40)
    # polygon(surface, color, points)
    pygame.draw.polygon(
        screen, black, [(115, 40), (75, 70), (105, 150), (36, 64)], True)
    # Hexagon
    pygame.display.flip()


draw_map()

start_pos = [10, 250-10]
validate(start_pos)
goal_pos = [390, 250-245]
validate(start_pos)    
pygame.time.wait(5000)

