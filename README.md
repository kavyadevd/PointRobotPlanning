# PointRobotPlanning
Planning for a point robot using Dijkstra algorithm

### Requirements
> Python 3
> Open CV

### Arena:
[<img src="https://user-images.githubusercontent.com/13993518/155918318-09e236c7-3c42-4aff-9fb0-e4e98eec9dd2.png" width="500" aligh="center"/>](https://user-images.githubusercontent.com/13993518/155918318-09e236c7-3c42-4aff-9fb0-e4e98eec9dd2.png)

### Steps to execute
```
python3 Dijkstra.py
```
Terminal will show the final path after computation is finished and a OpenCV showing robot exploration space will be launched.
On closing exploration space video, the final path plot visialisation can be seen<br>
Goal is indicated by green text on map


### Results

Original speed            |  4xspeed explore all  
:-------------------------:|:-------------------------:
![Output](https://user-images.githubusercontent.com/13993518/156872432-122d5210-cca9-4244-a886-e42fa8abdb55.gif)  |   ![Explore_all](https://user-images.githubusercontent.com/13993518/156871997-734635d7-056c-4f0d-b1c4-48816752d267.gif)
![Output](https://user-images.githubusercontent.com/13993518/156872747-05e95d3d-b182-44a7-8db1-dadec333d67a.png) | ![Output](https://user-images.githubusercontent.com/13993518/156872572-70ffd8b8-13cb-43b5-afb3-b2e35c9064c2.png)

  
 #### Path plot example
 ![PathPlot](https://user-images.githubusercontent.com/13993518/156872044-d384784f-81ac-4b7d-83c8-f8db6439ec1c.png)



### Note:
> Visulation done using Mathplotlib can be seen on branch [Mathplotlib](https://github.com/kavyadevd/PointRobotPlanning/tree/Mathplotlib)
> As this visualtion is slow becuase of Mathplotlib limitations, same visialisation was implemented using OpenCV which is present in the main branch.

### Move Logic

#### Find possible moves for each step
![<img src="https://user-images.githubusercontent.com/13993518/156101896-ff6c9c3d-aa50-43a5-a714-ca455f7346bc.png" width="250"/>](https://user-images.githubusercontent.com/13993518/156101896-ff6c9c3d-aa50-43a5-a714-ca455f7346bc.png)
<sup size="0.5">Figure 1: Possible moves</sup>


##### Weight for each action is as follows:
<img src="https://user-images.githubusercontent.com/13993518/156457885-275d718e-0ae2-457e-89c3-6ca22c3ab387.png" width="400"/>
<sup size="0.5">Figure 2: Weight of each action</sup>

