from env_gym_wrapper import GymEnvWrapper
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3 import PPO
from Create_maze import Maze_generator
# 0-->left 1-->right 2->down 3 -->up 


def main():
    dim=5
    maze_generator = Maze_generator(dim,dim)
    #check_env(env,warn=True)# Check if the env is corret according to gym standards
    
    num_envs = 4  # Number of parallel environments
    env = SubprocVecEnv([make_env(maze_generator) for _ in range(num_envs)])
    

    model = PPO("MlpPolicy",env,verbose=1, tensorboard_log="./ppo_tensorboard/")
    model.learn(total_timesteps=5000000, progress_bar=True)
    model.save("PPO")

def make_env(maze_generator):
    def _init():
        env = GymEnvWrapper(maze_generator) #Return a new instance of GymEnvWrapper
        env = Monitor(env)
        return env
    return _init


# print("done: ",done,"| info: ",info,"| observation: ",observation,"| reward: ",reward,"| truncated:",truncated)
if __name__ == "__main__":
    main()