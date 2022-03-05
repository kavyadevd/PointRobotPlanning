import matplotlib.path as mplPath
from Node import Node
from Robotplan import RobotPlan
import math


class Game:
    def __init__(self, start, goal, clearance, obstacle) -> None:
        self.start = start
        self.clearance = clearance
        self.goal = goal
        self.obstacle = obstacle

    def Start(self):
        point = []
        Current = Node(self.start, 0, None, None)
        Visted = [Current]
        AllNodes = {tuple(Current.gameparams)}
        distance = 500
        count = 1
        while (distance >= 1):
            if len(Visted) != 0:
                print('Computing', '.'*count)
                Current = Visted.pop()
                point.append(Current.gameparams)
                R = RobotPlan(self.clearance, Current.gameparams)
                moves = R.GetActions(self.obstacle, Current.moves)
                #print(moves)
                for e in moves:
                    xy = R.GetNewCoordinates(e)
                    xy = [(Current.gameparams[0]+xy[0]),
                          (Current.gameparams[1]+xy[1])]
                    #print('Current: ', (Current.gameparams[0]), ',', Current.gameparams[1], 'Action: ', e, ' : ', xy)
                    NextNode = Node(xy, 0, Current, e)
                    if tuple(xy) not in AllNodes:
                        Visted.append(NextNode)
                        AllNodes.add(tuple(xy))
                Visted.sort(key=lambda w: w.cost, reverse=True)
            else:
                return -1, Current.GetBacktrack(), point
            distance = (math.sqrt(
                ((Current.gameparams[0]-self.goal[0])**2) + ((Current.gameparams[1]-self.goal[1])**2)))
            count = (count+1) if count < 5 else 1
        points_ = Current.GetBacktrack()
        print('Dijkstra Completed')
        path = []
        for e in points_:
            path.append(e.gameparams)
        print('Point Robot path is :\n',path)
        return path, point


class Obstacle:
    def __init__(self, clearance, point, screen_height, screen_width, polygon1_shape, hexagon) -> None:
        self.height = screen_height
        self.width = screen_width
        self.clearance = clearance
        self.robot_pos = point
        self.obstacles = []
        self.polygon1_shape = polygon1_shape
        self.hexagon = hexagon

    # Calculates points of line paralle to side with translation = clearance (distance)
    def LineOffset(self, x1, x2, y1, y2, distance):
        points = []
        slope = (y2 - y1) / (x2 - x1)
        pslope = -1/slope
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        sign = ((pslope > 0) == (x1 > x2)) * 2 - 1
        delta_x = sign * distance / ((1 + pslope**2)**0.5)
        delta_y = pslope * delta_x
        points.append([mid_x + delta_x, mid_y + delta_y])
        return (x1 + delta_x), (y1 + delta_y), (x2 + delta_x), (y2 + delta_y)

    # Returns intersection point of two parallel points
    def GetIntersection(self, side1, side2):
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]
        x1_x2 = (side1[0][0] - side1[1][0], side2[0][0] - side2[1][0])
        y1_y2 = (side1[0][1] - side1[1][1], side2[0][1] - side2[1][1])
        div = det(x1_x2, y1_y2)
        d = (det(*side1), det(*side2))
        x = det(d, x1_x2) / div
        y = det(d, y1_y2) / div
        return x, y

    def GetShape1WithOffset(self, polygon_shape):
        polygon_shapenew = []
        tempx1, tempy1, tempx2, tempy2 = (self.LineOffset(
            polygon_shape[0][0], polygon_shape[1][0], polygon_shape[0][1], polygon_shape[1][1], -5))
        A = (tempx1, tempy1)
        B = (tempx2, tempy2)

        tempx, tempy, tempx2, tempy2 = (self.LineOffset(
            polygon_shape[2][0], polygon_shape[1][0], polygon_shape[2][1], polygon_shape[1][1], 5))
        C = (tempx, tempy)
        D = (tempx2, tempy2)
        x_, y_ = self.GetIntersection((A, B), (C, D))
        polygon_shapenew.append([x_, y_])

        tempx, tempy, tempx2, tempy2 = (self.LineOffset(
            polygon_shape[2][0], polygon_shape[3][0], polygon_shape[2][1], polygon_shape[3][1], -5))
        E = (tempx, tempy)
        F = (tempx2, tempy2)
        x, y = self.GetIntersection((C, D), (E, F))
        polygon_shapenew.append([x, y])

        tempx, tempy, tempx2, tempy2 = (self.LineOffset(
            polygon_shape[3][0], polygon_shape[0][0], polygon_shape[3][1], polygon_shape[0][1], -5))
        G = (tempx, tempy)
        H = (tempx2, tempy2)
        x, y = self.GetIntersection((E, F), (G, H))
        polygon_shapenew.append([x, y])

        x, y = self.GetIntersection((G, H), (A, B))
        polygon_shapenew.append([x, y])
        polygon_shapenew.append([x_, y_])

        return polygon_shapenew

    def GetHexagonWithOffset(self, hexagon):
        polygon_shapenew = []
        tempx1, tempy1, tempx2, tempy2 = (self.LineOffset(
            hexagon[0][0], hexagon[1][0], hexagon[0][1], hexagon[1][1], -5))
        A = (tempx1, tempy1)
        B = (tempx2, tempy2)

        C = (240, 120)
        D = (240, 80)
        x_, y_ = self.GetIntersection((A, B), (C, D))
        polygon_shapenew.append([x_, y_])

        tempx, tempy, tempx2, tempy2 = (self.LineOffset(
            hexagon[2][0], hexagon[3][0], hexagon[2][1], hexagon[3][1], -5))
        E = (tempx, tempy)
        F = (tempx2, tempy2)
        x, y = self.GetIntersection((C, D), (E, F))
        polygon_shapenew.append([x, y])

        tempx, tempy, tempx2, tempy2 = (self.LineOffset(
            hexagon[3][0], hexagon[4][0], hexagon[3][1], hexagon[4][1], -5))
        G = (tempx, tempy)
        H = (tempx2, tempy2)
        x, y = self.GetIntersection((E, F), (G, H))
        polygon_shapenew.append([x, y])

        I = (160, 120)
        J = (160, 80)
        x, y = self.GetIntersection((G, H), (I, J))
        polygon_shapenew.append([x, y])

        tempx, tempy, tempx2, tempy2 = (self.LineOffset(
            hexagon[5][0], hexagon[0][0], hexagon[5][1], hexagon[0][1], -5))
        K = (tempx, tempy)
        L = (tempx2, tempy2)
        x, y = self.GetIntersection((I, J), (K, L))
        polygon_shapenew.append([x, y])

        x, y = self.GetIntersection((K, L), (A, B))
        polygon_shapenew.append([x, y])
        polygon_shapenew.append([x_, y_])

        return polygon_shapenew

    def AddObstacle(self, shape, points):
        temp = []
        temp.append(shape)
        temp.append(points)
        self.obstacles.append(temp)
        if shape == 'circle':
            self.circle_center = points[0]
            self.circle_radius = points[1][0]

    # Checks if point is within pointspace
    def Validate(self, pos, height, width):
        if (pos[0] <= (self.clearance)) or (pos[0] >= (width-self.clearance)) or (pos[1] <= self.clearance) or (pos[1] >= (height-self.clearance)):
            # if self.clearance <= pos[0] >= (width-self.clearance) or self.clearance <= pos[1] >= (height-self.clearance):
            #print('Entered ponit ', pos, ' is not within map dimensions')
            return False
        return True

    # Use for Faster computation
    # def InsidePolygon(self, point, polygon_points) -> bool:
    #     polygon_shape = mplPath.Path(np.array(polygon_points))
    #     robot_pos = (point[0], point[1])
    #     flag = polygon_shape.contains_point(robot_pos)
    #     return flag

    # Check if point is inside polygon using intersection points method
    def InsidePolygon(self, point, vertices) -> bool:
        count = 0
        vertices = tuple(vertices[:])+(vertices[0],)
        for v in range(len(vertices)-1):
            if ((vertices[v][1] <= point[1] and vertices[v+1][1] > point[1])
                    or (vertices[v][1] > point[1] and vertices[v+1][1] <= point[1])):
                vx_intersect = (point[1] - vertices[v][1]) / \
                    float(vertices[v+1][1] - vertices[v][1])
                if point[0] < vertices[v][0] + vx_intersect * (vertices[v+1][0] - vertices[v][0]):
                    count += 1
        return ((count % 2) == 1)

    # Returns true if point in inside circle
    def InsideCircle(self, point) -> bool:
        # (x-x1)^2 + (y-y1)^2 <= (r+clearance)^2
        center = self.circle_center
        radius = self.circle_radius + self.clearance
        flag = ((point[0]-center[0])**2 + (point[1]-center[1])
                ** 2 <= (radius+self.clearance)**2)
        return flag

    # Calls all validation methods
    def ValidateAll(self, pos):
        if not self.Validate(pos, self.height, self.width):
            #print('Execute again and provide valide inputs')
            return False
        if self.InsideCircle(pos):
            #print('Point: ', pos, ' overlaps with ciclular obstacle')
            return False
        self.polygon_with_border = self.GetShape1WithOffset(
            self.polygon1_shape)
        if self.InsidePolygon(pos, self.polygon_with_border):
            #print('Point: ', pos, ' overlaps with obstacle')
            return False
        self.hexagon_with_border = self.GetHexagonWithOffset(self.hexagon)
        if self.InsidePolygon(pos, self.hexagon_with_border):
            return False
        return True
