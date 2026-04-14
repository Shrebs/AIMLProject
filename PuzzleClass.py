class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.open_list = []          # Priority queue for exploration
        self.closed_list = set()     # Visited states
        self.nodes_expanded = 0
        self.max_frontier_size = 0