def reconstruct_path(self, node):
    """Reconstruct solution path from start to goal"""
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = current.parent
    return path[::-1]  # Reverse to get start → goal