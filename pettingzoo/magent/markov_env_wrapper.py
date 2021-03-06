from pettingzoo.utils import agent_selector
from pettingzoo import AECEnv


class markov_env_wrapper(AECEnv):
    metadata = {'render.modes': ['human']}
    '''
    Parent Class Methods
    '''
    def __init__(self, markov_env):
        self.env = markov_env
        self.agents = self.env.agents
        self.num_agents = len(self.agents)

        self.action_spaces = {agent: space for agent, space in zip(self.agents, self.env.action_spaces)}
        self.observation_spaces = {agent: space for agent, space in zip(self.agents, self.env.observation_spaces)}
        self._agent_mapper = {agent: i for i, agent in enumerate(self.agents)}

    def reset(self, observe=True):
        self._actions = [None] * self.num_agents

        self._live_agents = self.agents[:]
        self._agent_selector = agent_selector(self._live_agents)
        self.agent_selection = self._agent_selector.reset()
        self.dones = {agent: False for agent in self.agents}
        self.infos = {agent: {} for agent in self.agents}
        self.rewards = {agent: 0 for agent in self.agents}

        self._observations = self.env.reset()

        return self.observe(self.agent_selection) if observe else None

    def observe(self, agent):
        return self._observations[self._agent_mapper[agent]]

    def step(self, action, observe=True):
        self._actions[self._agent_mapper[self.agent_selection]] = action
        if self._agent_selector.is_last():
            obss, rews, dones, infos = self.env.step(self._actions)
            self._observations = obss

            self.dones = {agent: done for agent, done in zip(self.agents, dones)}
            self.infos = {agent: info for agent, info in zip(self.agents, infos)}
            self.rewards = {agent: reward for agent, reward in zip(self.agents, rews)}

            self._live_agents = [agent for done, agent in zip(dones, self.agents) if not done]
            if len(self._live_agents):
                self._agent_selector = agent_selector(self._live_agents)
                self.agent_selection = self._agent_selector.reset()
        else:
            self.agent_selection = self._agent_selector.next()
        return self.observe(self.agent_selection) if observe else None

    def render(self, mode="human"):
        self.env.render()

    def close(self):
        self.env.close()
