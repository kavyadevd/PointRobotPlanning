class RobotPlan:
    def __init__(self, clearance, point) -> None:
        self.clearance = clearance
        self.robot_pos = point
    
    # Refer Possible Moves diagram in ReadMe
    def GetActions(self, obstacle, last_action):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        moves = []
        if not last_action:
            last_action = 'Z'
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
        return moves

    def GetNewCoordinates(self,action):
        if action == 'U':
            return [0,1] # increment y by 1
        if action == 'UR':
            return [1,1] # increment x,y by 1
        elif action == 'R':
            return [1,0] # increment x by 1
        elif action == 'DR':
            return [1,-1]
        elif action == 'D':
            return [0,-1] # decrement y by 1
        elif action == 'DL':
            return [-1,-1]
        elif action == 'L':
            return [-1,0] # decrement x by 1
        elif action == 'UL':
            return [-1,1]