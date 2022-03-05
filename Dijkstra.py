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

def PlotPath(path):
    xs, ys = zip(*path)
    plot.plot(xs,ys)

def DrawMap(points):
    # plot.subplots(121)
    plot.ylim([0, 250])
    plot.xlim([0, 400])

    #Polygon 1
    poly = polygon1_points
    poly.append(poly[0])
    xs, ys = zip(*poly)
    plot.plot(xs,ys)
    plot.fill(xs, ys, "c")

    # Plot start goal points
    plot.text(start_pos[0],start_pos[1],'Start')
    plot.text(goal_pos[0],goal_pos[1],'Goal')
    plot.plot(start_pos[0],start_pos[1], 'ro')
    plot.plot(goal_pos[0],goal_pos[1], 'ro')

    #Circle
    Drawing_colored_circle = plot.Circle(( 300 , 185 ), 40 )
    axes.add_artist( Drawing_colored_circle ) 

    #Hexagon
    poly = polygon2_points
    poly.append(poly[0])
    xs, ys = zip(*poly)
    plot.plot(xs,ys)
    plot.fill(xs, ys, "c")

    # Clearance
    poly = poly1_offset
    xs, ys = zip(*poly)
    plot.plot(xs,ys)

    poly = hexa_offset
    xs, ys = zip(*poly)
    plot.plot(xs,ys)


    circle_border = plot.Circle((300, 185), 45, color='r')
    axes.add_patch(circle_border)

    # Animate Dijkstra space
    poly = polygon2_points
    poly.append(poly[0])
    xs, ys = zip(*poly)
    global dataSet
    plot.plot(xs,ys)
    plot.fill(xs, ys, "c")

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    dataSet = np.array([xs, ys])
    
    line_ani = animation.FuncAnimation(fig1, animate_func, interval=1,   
                                   frames=len(points)//20)
    #line_ani.save('points.gif', writer='abc', fps=30)
    plot.show()
    line_ani.save('animation.gif', writer='PillowWriter', fps=30)

def animate_func(num):
    axes.plot(dataSet[0, :num+1], dataSet[1, :num+1])
    axes.scatter(dataSet[0, num], dataSet[1, num], marker='o')

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
    DrawMap(points)
    PlotPath(path)
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






