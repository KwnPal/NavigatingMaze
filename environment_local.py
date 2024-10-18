import numpy as np
import copy
from Agent import agent
from Create_maze import Maze_generator
import time

class Env_local:
    def __init__(self, Maze_generator):
        self.maze_gen = Maze_generator
        self.maze = self.maze_gen.generate_maze_dfs()
        self.env_id = Maze_generator.maze_id
        self.agent = agent(self.maze)
        self.createEnv()

    def createEnv(self):
        obs = {
            "high":[self.maze.height, self.maze.width],
            "low": 0
              }
        self.high = np.array(obs["high"])
        self.low = obs["low"]
        print("New env created \nEnv id: ", self.env_id)

    def reset(self):
        self.agent.agent_position = [0,0]
        observation = np.array(self.agent.agent_position, dtype = np.float32)
        self.maze = self.maze_gen.generate_maze_dfs()
        print("RESET")
        return observation 

            
    def step(self,action):
        reward, done = self.agent.action_update(action)
        observation = np.array(self.agent.agent_position, dtype = np.float32)
        truncated = False
        info = {}
        return observation, reward, done, truncated, info

    def print_agent(self):
        temp = copy.deepcopy(self.maze)
        temp.maze[self.agent.agent_position[0]][self.agent.agent_position[1]] = "A"
        temp.print_maze()


    
        
    # 0-->left 1-->right 2->down 3 -->up 

   

        
        