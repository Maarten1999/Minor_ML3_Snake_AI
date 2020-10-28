import logging

# import gym_snake  # don't use the registered snake
from gym_snake.envs.snake_env import SnakeEnv
from path_finding import path_finder

solver = path_finder.BFS()

log = logging.getLogger("miniproject_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

NOMOVE = -1
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

n_snakes = 2

# env = SnakeEnv(grid_size=[12, 12], snake_size=2, n_snakes=3, n_foods=3)
env = SnakeEnv(grid_size=[9, 9], snake_size=2, n_snakes=n_snakes, n_foods=2)
obs = env.reset()  # construct instance of game
done = n_snakes
turn = 0
log.info("start game")
while done > 0:
    env.render()

    if turn == 0:
        turn = 1
        action = solver.get_actions(obs, 9, 9)
        if len(action) > 0:
            obs, reward, d, info = env.step(int(action[0]))  # reward is for the snake that has moved
            if d:
                done -= 1
    elif turn == 1:
        turn = 0
        action = solver.get_actions(obs, 9, 9)
        if len(action) > 0:
            obs, reward, d, info = env.step(int(action[0]))  # reward is for the snake that has moved
            if d:
                done -= 1
env.close()
