import heapq
from NodeStructure import Node

class EightPuzzle:
    
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def find_blank(self, state):
        return state.index(0)
    
    def get_neighbors(self, state):
        blank = self.find_blank(state)
        row, col = blank // 3, blank % 3
        
        moves = [("UP",-1,0),("DOWN",1,0),("LEFT",0,-1),("RIGHT",0,1)]
        neighbors = []
        
        for name, r, c in moves:
            nr, nc = row+r, col+c
            if 0<=nr<3 and 0<=nc<3:
                new = list(state)
                new_pos = nr*3+nc
                new[blank], new[new_pos] = new[new_pos], new[blank]
                neighbors.append((tuple(new), name))
        
        return neighbors
    
    def manhattan(self, state):
        dist = 0
        for val in state:
            if val == 0: continue
            i = state.index(val)
            g = self.goal_state.index(val)
            dist += abs(i//3 - g//3) + abs(i%3 - g%3)
        return dist
    
    def reconstruct(self, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]
    
    def solve(self):
        open_list = []
        closed = set()
        
        start = Node(self.initial_state)
        start.h = self.manhattan(start.state)
        start.f = start.h
        
        heapq.heappush(open_list, (start.f, start))
        
        while open_list:
            _, current = heapq.heappop(open_list)
            
            if current.state == self.goal_state:
                return self.reconstruct(current)
            
            closed.add(current.state)
            
            for s, move in self.get_neighbors(current.state):
                if s in closed:
                    continue
                
                n = Node(s, current, move)
                n.g = current.g + 1
                n.h = self.manhattan(s)
                n.f = n.g + n.h
                
                heapq.heappush(open_list, (n.f, n))
        
        return None
