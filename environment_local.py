import numpy as np
import copy
from Agent import agent
from Create_maze import Maze_generator
import random
import time

class Env_local:
    env_id = 0
    def __init__(self, Maze_generator):
        Env_local.env_id +=1
        self.id = Env_local.env_id
        self.maze_gen = Maze_generator
        self.maze = self.maze_gen.generate_maze_dfs()
        self.agent = agent(self.maze)
        self.createEnv()

    def createEnv(self):
        obs = {
            "high":[self.maze.height, self.maze.width],
            "low": 0
              }
        self.high = np.array(obs["high"])
        self.low = obs["low"]
        print("New env created \nEnv id: ", self.id)

    def reset(self):
        self.agent.agent_position = [0,0]
        observation = np.array(self.agent.agent_position, dtype = np.float32)
        if self.maze_gen.seed is None:
            seed = random.randint(0, 99999999) 
            self.maze_gen.set_seed(seed)
        self.maze = self.maze_gen.generate_maze_dfs()
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

   

        
        