from gym.spaces import Discrete, Box
import numpy as np
import warnings
import magent
from pettingzoo import AECEnv
import math
from pettingzoo.magent.render import Renderer
from pettingzoo.utils import agent_selector, wrappers
from .magent_env import markov_env, make_env
from .markov_env_wrapper import markov_env_wrapper
from .battle import get_config


def raw_env(map_size=80, seed=None):
    return markov_env_wrapper(markov_env(map_size, seed))


env = make_env(raw_env)


class markov_env(markov_env):
    def __init__(self, map_size, seed):
        env = magent.GridWorld(get_config(map_size), map_size=map_size)
        self.leftID = 0
        self.rightID = 1
        names = ["red", "blue"]
        super().__init__(env, env.get_handles(), names, map_size, seed)

    def generate_map(self):
        env, map_size, handles = self.env, self.map_size, self.handles
        """ generate a map, which consists of two squares of agents"""
        width = height = map_size
        init_num = map_size * map_size * 0.04
        gap = 3

        width = map_size
        height = map_size

        init_num = 20

        gap = 3
        leftID, rightID = 0, 1

        # left
        pos = []
        for y in range(10, 45):
            pos.append((width / 2 - 5, y))
            pos.append((width / 2 - 4, y))
        for y in range(50, height // 2 + 25):
            pos.append((width / 2 - 5, y))
            pos.append((width / 2 - 4, y))

        for y in range(height // 2 - 25, height - 50):
            pos.append((width / 2 + 5, y))
            pos.append((width / 2 + 4, y))
        for y in range(height - 45, height - 10):
            pos.append((width / 2 + 5, y))
            pos.append((width / 2 + 4, y))
        env.add_walls(pos=pos, method="custom")

        n = init_num
        side = int(math.sqrt(n)) * 2
        pos = []
        for x in range(width // 2 - gap - side, width // 2 - gap - side + side, 2):
            for y in range((height - side) // 2, (height - side) // 2 + side, 2):
                pos.append([x, y, 0])
        env.add_agents(handles[leftID], method="custom", pos=pos)

        # right
        n = init_num
        side = int(math.sqrt(n)) * 2
        pos = []
        for x in range(width // 2 + gap, width // 2 + gap + side, 2):
            for y in range((height - side) // 2, (height - side) // 2 + side, 2):
                pos.append([x, y, 0])
        env.add_agents(handles[rightID], method="custom", pos=pos)
