import gymnasium as gym
from gymnasium import spaces
import numpy as np
from environment import Env

class GymEnvWrapper(gym.Wrapper):
    def __init__(self,Env):
        super().__init__(Env)
        
        self.
