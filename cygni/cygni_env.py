import numpy as np
import gym
from gym import spaces
from gym.utils import seeding
import logging

from cygni import util
from cygni import online_cygni

log = logging.getLogger("cygni_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


class CygniEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(CygniEnv, self).__init__()

        self.grid_size = [46, 34]  # default Cygni size
        # actions = [util.Direction.DOWN, util.Direction.LEFT, util.Direction.UP, util.Direction.RIGHT]
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=3, shape=(self.grid_size[1], self.grid_size[0]), dtype=np.uint8)

    def step(self, action):
        done = False
        reward = 0.0

        return np.array(self.state), reward, done, {}

    def reset(self):
        return np.array(self.state)

    def render(self, mode='human'):
        # TODO update with actual state
        log.info("time: %d, position: %0f, energy: %0f", self.timestep, self.state[0], self.state[1])

    def close(self):
        pass
