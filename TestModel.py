import gymnasium as gym

from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from envGymWrapper import GymEnvWrapper

url="http://3.77.211.177:5005"
env = GymEnvWrapper(url)

model = DQN.load("DQN", env=env)
obs , info =env.reset()
episode_reward= 0.0
for _ in range(1000):
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    episode_reward += reward
    if terminated or truncated or reward==100:
        print("Reward:", episode_reward, "Success?"," True" if reward == 100 else "False")
        episode_reward = 0.0
        obs, info = env.reset()