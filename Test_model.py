import numpy as np
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.evaluation import evaluate_policy
from env_gym_wrapper import GymEnvWrapper

url="http://3.77.211.177:5005"
env = GymEnvWrapper(url)

model = PPO.load("PPO", env=env)
obs , info =env.reset()

episodes=1 # The number of all the episodes
rewardAllEp = [] # A list containing the sum of rewards of each episode
stepsList = [] # A list containing the steps of every episode
epReward= 0.0 # The sum of rewards
goalAchieved = 0 # If the agent found the exit in the maze
steps=0
for episode in range(episodes):
    obs,info = env.reset()
    epReward = 0.0
    steps=0
    done = False

    while not done:
        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, info = env.step(action)
        steps += 1
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
