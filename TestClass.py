from environment import Env
from envGymWrapper import GymEnvWrapper
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import DQN
# 0-->left 1-->right 2->down 3 -->up 

url="http://3.77.211.177:5005"
env = GymEnvWrapper(url)

# env = GymEnvWrapper(url)
check_env(env,warn=True)

# model = DQN("MlpPolicy",env,verbose=2)
# model.learn(total_timesteps=200000, progress_bar=True)
# model.save("DQN")

# print("done: ",done,"| info: ",info,"| observation: ",observation,"| reward: ",reward,"| truncated:",truncated)
