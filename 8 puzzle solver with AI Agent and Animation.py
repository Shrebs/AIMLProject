import heapq
import time
import tkinter as tk

# ---------------- NODE ---------------- #
class Node:
    def __init__(self, state, parent=None, move="Start"):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __lt__(self, other):
        return self.f < other.f


# ---------------- PUZZLE LOGIC ---------------- #
class EightPuzzle:
    
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def get_neighbors(self, state):
        blank = state.index(0)
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
    
    def reconstruct(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]


# ---------------- GUI ---------------- #
class PuzzleGUI:
    
    def __init__(self, root, path):
        self.root = root
        self.path = path
        self.step = 0
        
        self.tiles = []
        
        for i in range(9):
            tile = tk.Label(
                root,
                text="",
                font=("Helvetica", 24, "bold"),
                width=4,
                height=2,
                borderwidth=2,
                relief="solid",
                bg="#1e90ff",
                fg="white"
            )
            tile.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.tiles.append(tile)
        
        self.update_board()
    
    def update_board(self):
        state = self.path[self.step]
        
        for i, val in enumerate(state):
            if val == 0:
                self.tiles[i].config(text="", bg="black")
            else:
                self.tiles[i].config(text=str(val), bg="#1e90ff")
        
        if self.step < len(self.path)-1:
            self.step += 1
            self.root.after(600, self.update_board)


# ---------------- AI AGENT ---------------- #
class Agent:
    
    def __init__(self, initial, goal):
        self.env = EightPuzzle(initial, goal)
    
    def perceive(self):
        print("[Agent] Observing environment...")
    
    def think(self):
        print("[Agent] Solving using A* + Manhattan...")
        return self.env.solve()
    
    def act(self, path):
        print("[Agent] Executing moves (visual)...")
        return path
    
    def run(self):
        self.perceive()
        path = self.think()
        return self.act(path)


# ---------------- MAIN ---------------- #
def main():
    initial = (1,2,3,4,0,5,6,7,8)

    goal = (1,2,3,4,5,6,7,8,0)
    
    agent = Agent(initial, goal)
    path = agent.run()
    
    if not path:
        print("No solution found")
        return
    
    root = tk.Tk()
    root.title("8 Puzzle AI Agent (A* + Manhattan)")
    
    app = PuzzleGUI(root, path)
    
    root.mainloop()


if __name__ == "__main__":
    main()