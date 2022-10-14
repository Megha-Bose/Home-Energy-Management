from headers import *
import agents.NS
import agents.PS
import agents.TS
import agents.Recommender
import agents.Filtering

ns_agents = [agents.NS.Agent()] * NUM_NS_AGENTS
ps_agents = [agents.PS.Agent()] * NUM_PS_AGENTS
ts_agents = [agents.TS.Agent()] * NUM_TS_AGENTS

recommender = agents.Recommender.Agent()
filtering = agents.Filtering.Agent()

if __name__ == "__main__":
    pass
