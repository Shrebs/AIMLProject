def main():
    # Define initial and goal states
    initial_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    # Create puzzle solver
    puzzle = EightPuzzle(initial_state, goal_state)
    
    # Solve using A*
    import time
    start_time = time.time()
    solution = puzzle.solve_astar()
    end_time = time.time()
    
    # Display results
    if solution:
        puzzle.display_solution(solution)
        print(f"\n✓ Solution found in {len(solution) - 1} moves")
        print(f"✓ Nodes expanded: {puzzle.nodes_expanded}")
        print(f"✓ Time taken: {end_time - start_time:.4f} seconds")
    else:
        print("✗ No solution found!")

if __name__ == "__main__":
    main()