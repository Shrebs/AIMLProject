class Node:
    def __init__(self, state, parent=None, move="Start"):
        self.state = state           # Puzzle configuration (tuple)
        self.parent = parent         # Parent node
        self.move = move             # Move description
        self.g = 0                   # Cost from start
        self.h = 0                   # Heuristic estimate
        self.f = 0                   # Total cost (g + h)