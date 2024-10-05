from environment import Env
from envGymWrapper import GymEnvWrapper
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3 import DQN
from stable_baselines3 import PPO
# 0-->left 1-->right 2->down 3 -->up 


def main():
    url="http://3.77.211.177:5005"

    # env = GymEnvWrapper(url)
    
    #check_env(env,warn=True)
    
    num_envs = 4  # Number of parallel environments
    env = SubprocVecEnv([make_env(url) for _ in range(num_envs)])


    model = DQN("MlpPolicy",env,verbose=1)
    model.learn(total_timesteps=25000,progress_bar=True)
    model.save("DQN")


def make_env(url):
    def _init():
        return GymEnvWrapper(url)  # Return a new instance of GymEnvWrapper
    return _init


# print("done: ",done,"| info: ",info,"| observation: ",observation,"| reward: ",reward,"| truncated:",truncated)
if __name__ == "__main__":
    main()