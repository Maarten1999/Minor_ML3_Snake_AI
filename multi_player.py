import logging

# import gym_snake  # don't use the registered snake
from gym_snake.envs.snake_env import SnakeEnv
from path_finding import path_finder

log = logging.getLogger("miniproject_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

NOMOVE = -1
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

n_snakes = 2
snakes = []
for i in range(n_snakes):
    snakes.append(path_finder.BFS())

# env = SnakeEnv(grid_size=[12, 12], snake_size=2, n_snakes=3, n_foods=3)
env = SnakeEnv(grid_size=[9, 9], snake_size=2, n_snakes=n_snakes, n_foods=2)
obs = env.reset()  # construct instance of game
done = n_snakes
turn = 0
log.info("start game")
while done > 0:
    env.render()

    actions_1 = snakes[0].get_actions(obs, 9, 9)
    actions_2 = snakes[1].get_actions(obs, 9, 9)

    if len(actions_1) == 0:
        done -= 1
    if len(actions_2) == 0:
        done -= 1

    total = len(actions_1) + len(actions_2)
    counter_1 = 0
    counter_2 = 0
    for i in range(total):
        action = -1
        if turn == 0:
            action = actions_1[counter_1]
            counter_1 += 1
        if turn == 0:
            action = actions_2[counter_2]
            counter_2 += 1
        turn += 1
        if turn >= n_snakes:
            turn = 0

        obs, reward, _, info = env.step(action)  # pass action to step()
        env.render()

    print(done)

    # # action = [DOWN, DOWN]  # *normal* multi-player snake: all snakes move at the same time
    # action = DOWN  # turn-based multi-player snake: one snake moves, other snakes don't move
    # obs, reward, done, info = env.step(action)  # reward is for the snake that has moved
    # log.info("reward: %.0f", reward)
env.close()
