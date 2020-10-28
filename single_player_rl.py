import logging

from stable_baselines import DQN
from stable_baselines.deepq.policies import MlpPolicy

# import gym_snake  # don't use the registered snake
from gym_snake.envs.snake_env import SnakeEnv

log = logging.getLogger("miniproject_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# actions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
#TODO: kleinere space
#TODO: reward functie aanpassen
env = SnakeEnv(grid_size=[24, 24], snake_size=2)
obs = env.reset()  # construct instance of game
contr = env.controller

training = False
if training:
    model = DQN(MlpPolicy, env, verbose=1)
    model.learn(total_timesteps=20000)
    model.save("./models/dqn_snake_single_player")
else:
    model = DQN.load("./models/dqn_snake_single_player")

print("finished training, now use the trained model and render the env")
n_episodes = 10

for i in range(n_episodes):
    obs = env.reset()
    done = False
    episode_steps = 0
    while not done:
        action, state = model.predict(obs)
        obs, reward, done, info = env.step(action)
        episode_steps += 1
        env.render()

    result = 'Succes!' if episode_steps < 200 else "Failure!"
    print(result)

env.close()
