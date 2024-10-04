import gymnasium as gym

from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy


# Create environment
env = gym.make("LunarLander-v2")

# Instantiate the agent
model = DQN("MlpPolicy",env, verbose=1)
# Train the agent and display a progress bar
model.learn(total_timesteps=int(200000), progress_bar=True)
# Save the agent
model.save("dqn_lunar2")
