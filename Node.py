
class Node:
    def __init__(self, puzzle, i, parent,moves):
        self.parent = parent
        self.index = i
        self.map_ = puzzle

        # set weight accoring to ReadMe Fig 2
        self.cost = 1 if  moves and (len(moves) == 1) else 1.4
        if not moves:
            self.cost = 0
        self.moves = moves
