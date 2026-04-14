def manhattan_distance(self, state):
    """Calculate Manhattan distance heuristic"""
    distance = 0
    for tile in state:
        if tile == 0:  # Skip blank
            continue
        
        # Current position
        current_pos = state.index(tile)
        current_row = current_pos // 3
        current_col = current_pos % 3
        
        # Goal position
        goal_pos = self.goal_state.index(tile)
        goal_row = goal_pos // 3
        goal_col = goal_pos % 3
        
        # Add Manhattan distance
        distance += abs(current_row - goal_row) + \
                    abs(current_col - goal_col)
    
    return distance