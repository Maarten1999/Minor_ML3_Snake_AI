import logging

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

env = SnakeEnv(grid_size=[6, 6], snake_size=2)
obs = env.reset()  # construct instance of game
done = False
log.info("start game")
for i in range(24):
    if not done:
        env.render()
        obs, reward, done, info = env.step(i % 4)  # pass action to step()
        log.info("reward: %.0f", reward)
env.close()
