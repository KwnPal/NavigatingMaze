import gymnasium as gym
import numpy as np
from environment_API import Env_API
from environment_local import Env_local
from gymnasium.spaces import Discrete, Box

class GymEnvWrapper(gym.Env):
    def __init__(self,Maze_generator):
        super().__init__()
        #self.Env=Env_API(url)# if API is used
        self.Env = Env_local(Maze_generator)
        self.id = self.Env.id
        self.action_space = Discrete(4)
        self.observation_space = Box(low = self.Env.low, high = self.Env.high, shape = (2,), dtype=np.float32)
        self.reset()

    #reset function returns observations as a np array and an empy info dic
    def reset(self,seed=None):
        #super().reset(seed=seed) #gym requires this call to control randomness and reproduce scenarios.
        ob = self.Env.reset(), {}
        return ob
    
    def step(self,action):
        observation,reward,done,truncated,info = self.Env.step(action)
        return observation,reward,done,truncated,info
        
    def print_agent(self):
        self.Env.print_agent()