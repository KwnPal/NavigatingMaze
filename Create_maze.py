import random
from Maze import maze

class Maze_generator:
    def __init__(self, width, height, seed = None):
        self.width = width
        self.height = height
        self.seed = seed
        self.maze_id = 0
    
    def __create_grid(self):# Creates a grid filled with zeroes
        grid =[[0 for _ in range(self.width)]for _ in range(self.height)]
        return grid
    
    def __is_in_bounds(self, x, y): # Prevents the algorithm move out of bounds
        return 0 <= x < self.width and 0 <= y < self.height
    
    def __carve_maze_dfs(self, grid, x, y):
    # Stack for backtracking
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = [(x, y)]
        grid[y][x] = 0
    
        while stack:
            current_x, current_y = stack[-1]
            
            # Find all unvisited neighbors (2 steps away in any direction)
            neighbors = []
            for dx, dy in DIRECTIONS:
                nx, ny = current_x + 2 * dx, current_y + 2 * dy
                if self.__is_in_bounds(nx, ny) and grid[ny][nx] == 0:
                    neighbors.append((nx, ny))
            
            if neighbors:
                # Choose a random neighbor to visit
                next_x, next_y = random.choice(neighbors)
                
                # Carve the path between current cell and next cell
                grid[current_y + (next_y - current_y) // 2][current_x + (next_x - current_x) // 2] = 1
                grid[next_y][next_x] = 1
                
                # Push the next cell to the stack
                stack.append((next_x, next_y))
            else:
                # Backtrack if no unvisited neighbors are left
                stack.pop()
        return grid
    
    def generate_maze_dfs(self):
    # Ensure odd dimensions for proper maze structure
        if self.width % 2 == 0:
            self.width += 1
            print("Warning! Even width found, converting to odd.. New width: ",self.width)
        if self.height % 2 == 0:
            self.height += 1
            print("Warning! Even height found, converting to odd.. New height: ",self.height)
        if self.seed is not None:
            random.seed(self.seed)
        # Create a grid filled with walls
        grid = self.__create_grid()
        grid = self.__carve_maze_dfs(grid, 0, 0)
        # Set the Start and Exit (For optical reasons)
        grid[self.height-1][self.width-1] = "E"

        self.maze_id += 1
        maze_instance = maze(self.width,self.height, self.maze_id, grid)

        return maze_instance
    
    def change_dim(self, width, height):
        self.width=width
        self.height=height

    def set_seed(self,seed):
        self.seed = seed