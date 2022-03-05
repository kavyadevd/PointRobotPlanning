class Node:
    def __init__(self,game_config, i, parent,moves):
        self.parent = parent
        self.index = i
        self.gameparams = game_config
        #self.map_ = puzzle

        # set weight accoring to ReadMe Fig 2
        if parent:
            self.cost = (self.parent.cost+1) if  moves and (len(moves) == 1) else (self.parent.cost+1.4)
        else :
            self.cost = (1) if  moves and (len(moves) == 1) else (1.4)
        if not moves:
            self.cost = 0
        self.moves = moves    

    def GetBacktrack(self):
        moves_= []
        # Backtrack
        node = self
        while node:
            moves_.append(node)
            node = node.parent
        yield from reversed(moves_)
