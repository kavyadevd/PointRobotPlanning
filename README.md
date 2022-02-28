# PointRobotPlanning
Planning for a point robot using Dijkstra algorithm

### Part 1 Create map
To create map and animate the robot motion here, *pygame* is used
> Install Pygame
```
pip install pygame
```
Generate map using the given dimensions
![image](https://user-images.githubusercontent.com/13993518/155918318-09e236c7-3c42-4aff-9fb0-e4e98eec9dd2.png)

> Pygame syntax to generate circle and polygon are as follows:
~~~~
pygame.draw.circle(surface, color, center, radius) 
pygame.draw.polygon(surface, color, points)
~~~~
