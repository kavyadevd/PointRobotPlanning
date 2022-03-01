from Obstacle import Obstacle

class RobotPlan:
    def __init__(self, clearance, point, screen_height, screen_width,startpoint, endpoint) -> None:
        self.height = screen_height
        self.width = screen_width
        self.clearance = clearance
        self.robot_pos = point
        self.startpoint = startpoint
        self.endpoint = endpoint
    
    # Refer Possible Moves diagram in ReadMe
    def GetActions(self, obstacle, last_action):
        moves = []        
        if last_action !='D' and obstacle.ValidateAll([self.robot_pos[0],self.robot_pos[1]+1]):
            moves.append('U')
        if last_action !='DL' and obstacle.ValidateAll([self.robot_pos[0]+1,self.robot_pos[1]+1]):
            moves.append('UR')
        if last_action !='L' and obstacle.ValidateAll([self.robot_pos[0]+1,self.robot_pos[1]]):
            moves.append('R')
        if last_action !='UL' and obstacle.ValidateAll([self.robot_pos[0]+1,self.robot_pos[1]-1]):
            moves.append('DR')
        if last_action !='U' and obstacle.ValidateAll([self.robot_pos[0],self.robot_pos[1]-1]):
            moves.append('D')
        if last_action !='UR' and obstacle.ValidateAll([self.robot_pos[0]-1,self.robot_pos[1]-1]):
            moves.append('DL')
        if last_action !='R' and obstacle.ValidateAll([self.robot_pos[0]-1,self.robot_pos[1]]):
            moves.append('L')
        if last_action !='DR' and obstacle.ValidateAll([self.robot_pos[0]-1,self.robot_pos[1]+1]):
            moves.append('UL')