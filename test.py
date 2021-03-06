from agents.dqn.dqn import DQN
from agents.ppo.ppo import PPO
from utils.runner import evaluate, make_env

if __name__ == "__main__":
    env = make_env()()

    agent = DQN(env.observation_space, env.action_space)
    #agent.load_model("agents/ppo/trained_models/ppo.pth")
    agent.load_model("modeleval.pth")
    returns = evaluate(agent, env, 100000, True, False, 0.05)