import numpy as np
from numba import jit

@jit(nopython=True)
def simulate_fire_history(width, height, density, steps):
    # Create a 3D array to hold the grid at every time step
    # Shape: (Total Steps + 1, Height, Width)
    history = np.zeros((steps + 1, height, width), dtype=np.uint8)
    
    # 0 = Ash (Black), 1 = Tree (Green), 2 = Fire (Red)
    grid = np.zeros((height, width), dtype=np.uint8)
    
    # 1. Plant the forest based on density
    for y in range(height):
        for x in range(width):
            if np.random.rand() < density:
                grid[y, x] = 1
                
    # 2. Ignite the center
    grid[height//2, width//2] = 2
    
    # Save the starting frame
    history[0] = grid.copy()
    
    # 3. Run the simulation
    for s in range(steps):
        new_grid = grid.copy()
        for y in range(1, height-1):
            for x in range(1, width-1):
                if grid[y, x] == 2:
                    new_grid[y, x] = 0 # Fire burns out into ash
                elif grid[y, x] == 1:
                    # Catch fire if a neighbor is burning
                    if (grid[y+1, x] == 2 or grid[y-1, x] == 2 or 
                        grid[y, x+1] == 2 or grid[y, x-1] == 2):
                        new_grid[y, x] = 2
        grid = new_grid
        # Save the current frame to our history array
        history[s + 1] = grid.copy()
        
    return history