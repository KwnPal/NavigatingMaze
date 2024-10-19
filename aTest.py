import os
from Create_maze import Maze_generator
from environment_local import Env_local


def main():
    dim=5
    maze_generator = Maze_generator(dim,dim)

    env = Env_local(maze_generator)

    
    env.maze.print_maze()
    env.reset()
    env.maze.print_maze()
    # env.maze.print_maze()
    # os.system("cls")
    # env.reset()
    # env.step(2)
    # env.step(2)
    # env.step(2)
    # env.step(0)
    # env.step(1)
    # env.step(3)
    # env.step(3)
    # env.step(1)
    # env.step(2)
    # env.step(3)
    # env.step(1)
    # env.step(1)
    # env.step(2)
    # env.step(2)
   




# 0-->left 1-->right 2->down 3 -->up 
if __name__ == "__main__":
    main()