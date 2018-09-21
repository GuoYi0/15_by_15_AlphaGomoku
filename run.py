from AlphaRenju_Zero import *
import warnings
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings("ignore")

print('> Please enter the mode: (1: Training, 2: AI vs Human, 3: Human vs Human, '
      '4: AI vs AI, 5: Collect human play data, 6: Collect self play data, '
      '7: Train on external data, 8: Collect human vs AI play data mode, '
      '9: AI(NaiveAgent) vs Human mode, 10: AI vs AI(NaiveAgent) mode), '
      '11: Train on generated data, 12: Collect self play data(Fast AI)')
mode = int(input('> mode = '))

if mode == 2:
    print('> Please select your color: (1: Black, 0: White)')
    is_black = int(input('> color = '))
    if is_black == 1:
        mode = 2.5

conf = Config()
conf.set_mode(mode)
env = Env(conf)

if mode == 1 or mode == 0:
    env.train()
if mode in [2, 2.5, 3, 9, 10]:
    env.run(use_stochastic_policy=False)
if mode == 4:
    env.mcts_vs_fast(game_num=20)
if mode == 5:
    env.collect_human_data()
if mode in [6, 12]:
    env.collect_self_play_data()
if mode == 7:
    env.train_on_external_data()
if mode == 8:
    env.collect_human_vs_ai_data()
if mode == 11:
    env.train_on_generated_data()
