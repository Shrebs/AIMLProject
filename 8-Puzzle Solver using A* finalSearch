import heapq
from collections import deque
import time

class Node:
    """Represents a state in the puzzle search tree"""
    def __init__(self, state, parent=None, move="Start"):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = 0  # Cost from start
        self.h = 0  # Heuristic
        self.f = 0  # Total cost
    
    def __lt__(self, other):
        """Comparison for priority queue"""
        return self.f < other.f


class EightPuzzle:
    """8-Puzzle solver using A* algorithm"""
    
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.open_list = []
        self.closed_list = set()
        self.nodes_expanded = 0
        self.max_frontier_size = 0
    
    def find_blank(self, state):
        """Find position of blank (0) in state"""
        return state.index(0)
    
    def get_neighbors(self, state):
        """Generate all valid neighboring states"""
        blank_pos = self.find_blank(state)
        row, col = blank_pos // 3, blank_pos % 3
        neighbors = []
        
        moves = [
            ("UP", -1, 0),
            ("DOWN", 1, 0),
            ("LEFT", 0, -1),
            ("RIGHT", 0, 1)
        ]
        
        for direction, row_offset, col_offset in moves:
            new_row = row + row_offset
            new_col = col + col_offset
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_pos = new_row * 3 + new_col
                state_list = list(state)
                state_list[blank_pos], state_list[new_pos] = \
                    state_list[new_pos], state_list[blank_pos]
                neighbors.append((tuple(state_list), direction))
        
        return neighbors
    
    def manhattan_distance(self, state):
        """Calculate Manhattan distance heuristic"""
        distance = 0
        for tile in state:
            if tile == 0:
                continue
            
            current_pos = state.index(tile)
            current_row = current_pos // 3
            current_col = current_pos % 3
            
            goal_pos = self.goal_state.index(tile)
            goal_row = goal_pos // 3
            goal_col = goal_pos % 3
            
            distance += abs(current_row - goal_row) + \
                       abs(current_col - goal_col)
        
        return distance
    
    def is_goal(self, state):
        """Check if state is goal"""
        return state == self.goal_state
    
    def reconstruct_path(self, node):
        """Reconstruct solution path"""
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = current.parent
        return path[::-1]
    
    def solve_astar(self):
        """Main A* search algorithm"""
        start_node = Node(self.initial_state)
        start_node.g = 0
        start_node.h = self.manhattan_distance(self.initial_state)
        start_node.f = start_node.h
        
        heapq.heappush(self.open_list, 
                      (start_node.f, id(start_node), start_node))
        
        while self.open_list:
            self.max_frontier_size = max(self.max_frontier_size, 
                                        len(self.open_list))
            
            _, _, current_node = heapq.heappop(self.open_list)
            
            if self.is_goal(current_node.state):
                return self.reconstruct_path(current_node)
            
            self.closed_list.add(current_node.state)
            self.nodes_expanded += 1
            
            for neighbor_state, direction in \
                    self.get_neighbors(current_node.state):
                
                if neighbor_state in self.closed_list:
                    continue
                
                neighbor_node = Node(neighbor_state, 
                                    current_node, direction)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = self.manhattan_distance(neighbor_state)
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                
                heapq.heappush(self.open_list, 
                              (neighbor_node.f, id(neighbor_node), 
                               neighbor_node))
        
        return None
    
    def print_puzzle_state(self, state, step=0, g=0, h=0, f=0):
        """Display puzzle state"""
        print(f"\nStep {step} | g(n)={g} | h(n)={h} | f(n)={f}")
        print("-" * 30)
        for i in range(3):
            row = state[i*3:(i+1)*3]
            print("| ", end="")
            for tile in row:
                print("_" if tile == 0 else tile, end=" | ")
            print()
        print("-" * 30)
    
    def display_solution(self, path):
        """Display complete solution"""
        print("\n" + "="*50)
        print("SOLUTION PATH")
        print("="*50)
        
        for step, node in enumerate(path):
            self.print_puzzle_state(
                node.state,
                step=step,
                g=node.g,
                h=node.h,
                f=node.f
            )


def main():
    # Define states
    initial_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    # Solve
    puzzle = EightPuzzle(initial_state, goal_state)
    
    start_time = time.time()
    solution = puzzle.solve_astar()
    end_time = time.time()
    
    # Results
    if solution:
        puzzle.display_solution(solution)
        print(f"\n{'='*50}")
        print("SOLUTION STATISTICS")
        print(f"{'='*50}")
        print(f"✓ Solution Length: {len(solution) - 1} moves")
        print(f"✓ Nodes Expanded: {puzzle.nodes_expanded}")
        print(f"✓ Max Frontier Size: {puzzle.max_frontier_size}")
        print(f"✓ Time Taken: {end_time - start_time:.4f} seconds")
    else:
        print("✗ No solution found!")


if __name__ == "__main__":
    main()
