import logging

import gym
import numpy as np
from gym import spaces

from cygni import util

log = logging.getLogger("cygni_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


class CygniEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, train_steps):
        super(CygniEnv, self).__init__()

        self.current_step = 0
        self.steps = train_steps
        self.state = np.array(self.read_map(train_steps[self.current_step]))
        print(self.state)
        self.snake_pos = [0, 0]

        self.grid_size = [46, 34]  # default Cygni size
        self.actions = [util.Direction.DOWN, util.Direction.LEFT, util.Direction.UP, util.Direction.RIGHT]
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=3, shape=self.state.shape,
                                            dtype=np.uint8)  # shape = array of 5 [Down, Left, Up, Right, Food_Direction]
        # self.observation_space = spaces.Box(low=0, high=3, shape=(self.grid_size[1], self.grid_size[0]), dtype=np.uint8)

    def step(self, action):
        done = False
        reward = 0.0
        next_pos = [0, 0]
        next_pos_value = 0

        # # look up snake head pos
        # for x in range(len(self.state)):
        #     for y in range(len(self.state[x])):
        #         if self.state[x][y] == 2:
        #             self.snake_pos = [x, y]

        # calculate next pos coordinates
        # if action == util.Direction.LEFT:
        #     next_pos = [self.snake_pos[0] - 1, self.snake_pos[1]]
        # elif action == util.Direction.RIGHT:
        #     next_pos = [self.snake_pos[0] + 1, self.snake_pos[1]]
        # elif action == util.Direction.UP:
        #     next_pos = [self.snake_pos[0], self.snake_pos[1] - 1]
        # elif action == util.Direction.DOWN:
        #     next_pos = [self.snake_pos[0], self.snake_pos[1] + 1]

        if action == util.Direction.LEFT:
            next_pos_value = self.state[1]
        elif action == util.Direction.RIGHT:
            next_pos_value = self.state[3]
        elif action == util.Direction.UP:
            next_pos_value = self.state[2]
        elif action == util.Direction.DOWN:
            next_pos_value = self.state[0]

            # calculate reward based on result after moving to next pos
        # if self.state[next_pos[0], next_pos[1]] == 1:
        #     reward -= 5  # punish for hitting anything
        #     done = True
        # elif next_pos[0] > self.grid_size[0] < next_pos[0] \
        #         or next_pos[1] > self.grid_size[1] < next_pos[1]:
        #     reward -= 5  # punish for going out of map
        #     done = True
        # elif self.state[next_pos[0], next_pos[1]] == 3:
        #     reward += 10
        # else:
        #     reward += -0.1  # punish for doing nothing (warning, might decide to running into walls to avoid this)

        if next_pos_value == 1:
            reward -= 1  # punish for hitting anything
            done = True
        elif next_pos_value == 3:
            reward += 1
        else:
            reward += 0  # punish for doing nothing (warning, might decide to running into walls to avoid this)

        self.current_step += 1
        if self.current_step >= len(self.steps):
            self.current_step = 0  # TODO move on to next environment

        self.state = self.read_map(self.steps[self.current_step])

        return np.array(self.state), reward, done, {}

    def reset(self):
        self.current_step = 0
        self.state = self.read_map(self.steps[self.current_step])
        return np.array(self.state)

    def render(self, mode='human'):
        # TODO update with actual state
        log.info("time: %d, position: %0f, energy: %0f", self.current_step, self.state[0], self.state[1])

    def close(self):
        pass

    def read_map(self, msg):
        width = msg['map']['width']
        height = msg['map']['height']
        environment_map = [0.] * width * height

        snakes = msg['map']['snakeInfos']
        for s in snakes:
            isHead = False

            if s['name'] == "snake.py":
                isHead = True

            for p in s['positions']:
                if isHead:
                    environment_map[p] = 2.
                    isHead = False
                else:
                    environment_map[p] = 1.

        obstacles = msg['map']['obstaclePositions']
        for s in obstacles:
            environment_map[s] = 1.

        food = msg['map']['foodPositions']
        for s in food:
            environment_map[s] = 3.

        # return np.reshape(environment_map, (height, width))

        return util.minimize_obs_space(np.reshape(environment_map, (height, width)))
