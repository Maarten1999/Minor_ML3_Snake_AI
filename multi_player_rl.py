import logging

from stable_baselines import DQN
from stable_baselines.deepq.policies import MlpPolicy

# import gym_snake  # don't use the registered snake
from gym_snake.envs.snake_env import SnakeEnv

log = logging.getLogger("miniproject_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# TODO: reward functie aanpassen
n_snakes = 2

# env = SnakeEnv(grid_size=[12, 12], snake_size=2, n_snakes=3, n_foods=3)
env = SnakeEnv(grid_size=[9, 9], snake_size=2, n_snakes=n_snakes, n_foods=2)
obs = env.reset()  # construct instance of game

contr = env.controller

training = False
if training:
    model = DQN(MlpPolicy, env, verbose=1, tensorboard_log="./tensorboard_logs/multi/")
    model.learn(total_timesteps=1000000)
    model.save("./models/dqn_snake_multi_player")
else:
    model = DQN.load("./models/dqn_snake_multi_player")

print("finished training, now use the trained model and render the env")
n_episodes = 1

turn = 0
done_running = n_snakes
while done_running > 0:
    env.render()

    if turn == 0:
        turn = 1
        action, state = model.predict(obs)
        obs, reward, done, info = env.step(action)
        if done:
            done_running -= 1
        env.render()

    elif turn == 1:
        turn = 0
        action, state = model.predict(obs)
        obs, reward, done, info = env.step(action)
        if done:
            done_running -= 1
        env.render()

env.close()
