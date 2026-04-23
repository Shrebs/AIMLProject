import tkinter as tk

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
