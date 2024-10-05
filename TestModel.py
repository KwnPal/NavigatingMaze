import gymnasium as gym

from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from envGymWrapper import GymEnvWrapper

url="http://3.77.211.177:5005"
env= GymEnvWrapper(url)

model = DQN.load("DQN", env=env)
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(10000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = vec_env.step(action)
