from classes import Cow
from rl_utils import init_Qtable

Ferdinand = Cow()

qtable = init_Qtable()

i = 0
while i<10:
    action = Ferdinand.get_action(qtable)
    Ferdinand.act(action)
    
    Ferdinand.evaluate()
    # Ferdinand.act(action)
    i+=1