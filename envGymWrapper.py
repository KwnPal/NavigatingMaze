import gymnasium as gym
import numpy as np
from environment import Env
from gymnasium.spaces import Discrete, Box
from typing import Optional

class GymEnvWrapper(gym.Env):
    def __init__(self,url):
        super().__init__()
        self.APIEnv=Env(url)
        self.action_space = Discrete(4)
        self.observation_space = Box(low = self.APIEnv.low, high = self.APIEnv.high, shape = (2,), dtype=np.float32)
        self.reset()
    #reset function returns observations as a np array and an empy info dic
    def reset(self,seed=None):
        # super().reset(seed=seed) #gym requires this call to control randomness and reproduce scenarios.
        ob = self.APIEnv.resetEnv(), {}
        return ob
    
    def step(self,action):
        observation,reward,done,truncated,info = self.APIEnv.step(action)
        # self.printMaze(observation)
        return observation,reward,done,truncated,info
    
    def render(self, mode='human'):
        pass

    def printMaze(self,obs):
        list= [[0 for j in range(5)]for i in range(5)]
        list[int(obs[0])][int(obs[1])] = 1
        for i in list:
            print(i)
        print("--------------------")
        