from environment import Env
from envGymWrapper import GymEnvWrapper
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3 import DQN
# 0-->left 1-->right 2->down 3 -->up 


def main():
    url="http://3.77.211.177:5005"

    # env = GymEnvWrapper(url)
    
    #check_env(env,warn=True)
    
    num_envs = 2  # Number of parallel environments
    env = SubprocVecEnv([make_env(url) for _ in range(num_envs)])


    model = DQN("MlpPolicy",env,verbose=2)
    model.learn(total_timesteps=200000, progress_bar=True)
    model.save("DQN")


def make_env(url):
    return GymEnvWrapper(url)


# print("done: ",done,"| info: ",info,"| observation: ",observation,"| reward: ",reward,"| truncated:",truncated)
if __name__ == "__main__":
    main()