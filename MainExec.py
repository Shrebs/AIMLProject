from PuzzleClass import EightPuzzle
from Visualization import PuzzleGUI
import tkinter as tk


class Agent:
    
    def __init__(self, initial, goal):
        self.env = EightPuzzle(initial, goal)
    
    def perceive(self):
        print("[Agent] Observing environment...")
    
    def think(self):
        print("[Agent] Solving using A* + Manhattan...")
        return self.env.solve()
    
    def act(self, path):
        print("[Agent] Executing solution...")
        return path
    
    def run(self):
        self.perceive()
        path = self.think()
        return self.act(path)


def main():
    initial = (2,8,3,1,6,4,7,0,5)
    goal = (1,2,3,4,5,6,7,8,0)
    
    agent = Agent(initial, goal)
    path = agent.run()
    
    if not path:
        print("No solution found")
        return
    
    root = tk.Tk()
    root.title("8 Puzzle AI Agent")
    
    gui = PuzzleGUI(root, path)
    root.mainloop()


if __name__ == "__main__":
    main()
