import json
import logging
import os
from random import Random

from stable_baselines import DQN
from stable_baselines.deepq.policies import MlpPolicy

# import gym_snake  # don't use the registered snake
from cygni.cygni_rl.cygni_env import CygniEnv

log = logging.getLogger("miniproject_snake")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# actions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

recordedSessions = []
total_train_steps = 1000000

# TODO: kleinere space
for file in os.listdir("../train_sessions"):
    if file.startswith("session"):
        with open("../train_sessions/" + file) as f:
            recordedSessions.append(json.load(f))

randNr = Random().randint(0, len(recordedSessions)-1)
env = CygniEnv(recordedSessions[randNr])
obs = env.reset()  # construct instance of game

model = DQN(MlpPolicy, env, verbose=1, tensorboard_log="./tensorboard_logs/single/")
print("Training...")
model.learn(total_timesteps=total_train_steps)
model.save("./models/dqn_cygni_snake")
