import logging

from stable_baselines import DQN
from stable_baselines.deepq.policies import MlpPolicy

# import gym_snake  # don't use the registered snake
from gym_snake.envs.snake_env import SnakeEnv

log = logging.getLogger("miniproject_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# TODO: reward functie aanpassen

env = SnakeEnv(grid_size=[9, 9], snake_size=2)
obs = env.reset()  # construct instance of game
contr = env.controller

training = True
if training:
    model = DQN(MlpPolicy, env, verbose=1, tensorboard_log="./tensorboard_logs/single/")
    model.learn(total_timesteps=1000000)
    model.save("./models/dqn_snake_single_player")
else:
    model = DQN.load("./models/dqn_snake_single_player")

print("finished training, now use the trained model and render the env")
n_episodes = 1

for i in range(n_episodes):
    done = False
    while not done:
        action, state = model.predict(obs)
        obs, reward, done, info = env.step(action)
        env.render()

env.close()
