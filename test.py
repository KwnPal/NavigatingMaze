import gymnasium as gym

from stable_baselines3 import SAC
from stable_baselines3.common.env_util import make_vec_env

vec_env = make_vec_env("Pendulum-v1", n_envs=4, seed=0)

# We collect 4 transitions per call to `env.step()`
# and performs 2 gradient steps per call to `env.step()`
# if gradient_steps=-1, then we would do 4 gradients steps per call to `env.step()`
model = SAC("MlpPolicy", vec_env, train_freq=1, gradient_steps=-1, verbose=1)
model.learn(total_timesteps=10_000,progress_bar=True)
model.save("SAC")