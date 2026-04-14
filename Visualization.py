def print_puzzle_state(self, state, step=0, g=0, h=0, f=0):
    """Display puzzle state as 3x3 grid"""
    print(f"\nStep {step} | g(n)={g} | h(n)={h} | f(n)={f}")
    print("-" * 20)
    for i in range(3):
        row = state[i*3:(i+1)*3]
        print("|", end=" ")
        for tile in row:
            if tile == 0:
                print("_", end=" | ")
            else:
                print(tile, end=" | ")
        print()
    print("-" * 20)

def display_solution(self, path):
    """Display complete solution path"""
    print("\n" + "="*40)
    print("SOLUTION PATH")
    print("="*40)
    
    for step, node in enumerate(path):
        self.print_puzzle_state(
            node.state, 
            step=step,
            g=node.g,
            h=node.h,
            f=node.f
        )