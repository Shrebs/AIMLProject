def get_neighbors(self, state):
    """Generate all valid adjacent states"""
    blank_pos = self.find_blank(state)
    row, col = blank_pos // 3, blank_pos % 3
    neighbors = []
    
    # Define valid moves: (direction, new_row_offset, new_col_offset)
    moves = [
        ("UP", -1, 0),
        ("DOWN", 1, 0),
        ("LEFT", 0, -1),
        ("RIGHT", 0, 1)
    ]
    
    for direction, row_offset, col_offset in moves:
        new_row = row + row_offset
        new_col = col + col_offset
        
        # Check boundaries
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            state_list = list(state)
            # Swap blank with adjacent tile
            state_list[blank_pos], state_list[new_pos] = \
                state_list[new_pos], state_list[blank_pos]
            neighbors.append((tuple(state_list), direction))
    
    return neighbors