import numpy as np
import airsim

# CHANGED (gym updated to gymnasium)
import gymnasium
from gymnasium import spaces

# CHANGED (Now inherits from gymnasium.Env)
class AirSimEnv(gymnasium.Env):
    # CHANGED (Now, render_modes is utilized)
    metadata = {"render_modes": ["rgb_array"]}

    def __init__(self, image_shape):
        self.observation_space = spaces.Box(0, 255, shape=image_shape, dtype=np.uint8)
        self.viewer = None

    def __del__(self):
        raise NotImplementedError()

    def _get_obs(self):
        raise NotImplementedError()

    def _compute_reward(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def step(self, action):
        raise NotImplementedError()

    def render(self):
        return self._get_obs()
