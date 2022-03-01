import matplotlib.path as mplPath
import numpy as np


class Obstacle:
    def __init__(self, clearance, point, screen_height, screen_width, polygon1_shape) -> None:
        self.height = screen_height
        self.width = screen_width
        self.clearance = clearance
        self.robot_pos = point
        self.obstacles = []
        self.polygon1_shape = polygon1_shape

    def AddObstacle(self, shape, points):
        temp = []
        temp.append(shape)
        temp.append(points)
        self.obstacles.append(temp)
        if shape == 'circle':
            self.circle_center = points[0]
            self.circle_radius = points[1][0]

    def Validate(self, pos, height, width):
        if self.clearance <= pos[0] >= (width-self.clearance) or self.clearance <= pos[1] >= (height-self.clearance):
            print('Entered ponit ', pos, ' is not within map dimensions')
            return False
        return True

    def InsidePolygon(self, point, polygon_points) -> bool:
        polygon_shape = mplPath.Path(np.array(polygon_points))
        robot_pos = (point[0], point[1])
        flag = polygon_shape.contains_point(robot_pos)
        return flag

    # Returns true if point in inside circle
    def InsideCircle(self, point) -> bool:
        # (x-x1)^2 + (y-y1)^2 <= (r+clearance)^2
        center = self.circle_center
        radius = self.circle_radius
        flag = ((point[0]-center[0])**2 + (point[1]-center[1])
                ** 2 <= (radius+self.clearance)**2)
        return flag

    def ValidateAll(self, pos):
        if not self.Validate(pos, self.height, self.width):
            print('Execute again and provide valide inputs')
        if self.InsideCircle(pos):
            print('Point: ', pos, ' overlaps with ciclular obstacle')
            return False
        if self.InsidePolygon(pos, self.polygon1_shape):
            print('Point: ', pos, ' overlaps with obstacle')
            return False
        return True
