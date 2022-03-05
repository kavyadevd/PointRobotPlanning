# PointRobotPlanning
Planning for a point robot using Dijkstra algorithm

### Part 1 Create map
To create map and animate the robot motion here, *pygame* is used
> Install Pygame
```
pip install pygame
```

[<img src="https://user-images.githubusercontent.com/13993518/155918318-09e236c7-3c42-4aff-9fb0-e4e98eec9dd2.png" width="500" aligh="center"/>](https://user-images.githubusercontent.com/13993518/155918318-09e236c7-3c42-4aff-9fb0-e4e98eec9dd2.png)

> Pygame syntax to generate circle and polygon are as follows:
~~~~
pygame.draw.circle(surface, color, center, radius) 
pygame.draw.polygon(surface, color, points)
~~~~

### Find possible moves for each step
![<img src="https://user-images.githubusercontent.com/13993518/156101896-ff6c9c3d-aa50-43a5-a714-ca455f7346bc.png" width="250"/>](https://user-images.githubusercontent.com/13993518/156101896-ff6c9c3d-aa50-43a5-a714-ca455f7346bc.png)
<sup size="0.5">Figure 1: Possible moves</sup>


#### Weight for each action is as follows:
<img src="https://user-images.githubusercontent.com/13993518/156457885-275d718e-0ae2-457e-89c3-6ca22c3ab387.png" width="400"/>
<sup size="0.5">Figure 2: Weight of each action</sup>


#### References
1. [Clearance offset calculation](https://stackoverflow.com/a/32773111/5155957)
2. [Calculate intersection of two lines](https://stackoverflow.com/a/20679579/5155957)
