from AlphaGomoku import *
import warnings
import os


if __name__ == '__main__':
    # ignore warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    warnings.filterwarnings("ignore")

    conf = Config()
    conf.set_mode(4)
    env = Env(conf)

    env.set_mcts_agent_version(agent_1_ver=23, agent_2_ver=19)
    env.start_mode()