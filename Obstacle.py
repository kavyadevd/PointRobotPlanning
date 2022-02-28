import matplotlib.path as mplPath
import numpy as np


class Obstacle:
    def __init__(self, clearance, point) -> None:
        self.clearance = clearance
        self.robot_pos = point

    def AddObstacle(self, shape, points):
        self.Obstacles.append(shape, points)
        if shape == 'circle':
            self.circle_center = points[0]
            self.circle_radius = points[1][0]

    def Validate(self, pos, height, width):
        if self.clearance <= pos[0] >= (width-self.clearance) or self.clearance <= pos[1] >= (height-self.clearance):
            print('Entered ponit ',pos,' is not within map dimensions')
            return False
        return True

    def InsidePolygon(self, point, polygon_points) -> bool:
        polygon_shape = mplPath.Path(np.array([polygon_points]))
        robot_pos = (point[0], point[1])
        return polygon_shape.contains_point(robot_pos)

    # Returns true if point in inside circle
    def InsideCircle(self, point) -> bool:
        # (x-x1)^2 + (y-y1)^2 <= (r+clearance)^2
        center = self.circle_center
        radius = self.circle_radius
        return (point[0]-center[0])**2 + (point[1]-center[1])**2 <= (radius+self.clearance)**2
