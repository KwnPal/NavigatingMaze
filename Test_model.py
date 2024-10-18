import numpy as np
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.evaluation import evaluate_policy
from env_gym_wrapper import GymEnvWrapper
from Create_maze import Maze_generator
from tqdm import tqdm
import time
# 0-->left 1-->right 2->down 3 -->up 
#url="http://3.77.211.177:5005"
load_path = "models\\"
dim=5
maze_generator = Maze_generator(dim,dim)
env = GymEnvWrapper(maze_generator)

model = DQN.load(load_path+"DQN_random")
obs , info =env.reset()

episodes=100 # The number of all the episodes
rewardAllEp = [] # A list containing the sum of rewards of each episode
stepsList = [] # A list containing the steps of every episode
epReward= 0.0 # The sum of rewards
goalAchieved = 0 # If the agent found the exit in the maze
steps=0
for episode in tqdm(range(episodes), desc = "Episodes completed"):
    obs,info = env.reset()
    epReward = 0.0
    steps=0
    done = False

    while not done:
        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, info = env.step(int(action))
        # print("New Obs: ",obs," action: ",action)
        # env.print_agent()
        steps += 1
        # if steps == 100:
        #     truncated = True
        epReward += reward
        done = terminated or truncated

    rewardAllEp.append(epReward)
    stepsList.append(steps)
    goalAchieved += (1 if reward == 100 else 0)
    print("Episode",episode + 1,"Reward:",epReward,"Success:" ,reward," Steps: ",steps) # if reward == 100 that means success = True
                                                                                        # anything else means False
temp= (goalAchieved / episodes) * 100 # Prediction score (%)
print("Prediction Score (%)",temp)
temp = (np.sum(stepsList)/episodes) # Mean of steps
print("Mean of Steps: ",temp)
temp= np.mean(rewardAllEp) # Mean reward
print("Mean reward",temp)
temp= np.std(rewardAllEp) # Standard deviation of rewards
print("Standard Deviation",temp)
