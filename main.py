from classes import Cow
from rl_utils import init_Qtable

Ferdinand = Cow()

qtable = init_Qtable()

i = 0
while i<10:
    print("Position", Ferdinand.right, Ferdinand.left, Ferdinand.hips)
    action = Ferdinand.get_action(qtable)
    print("Action" , action)
    Ferdinand.act(action)
    
    Ferdinand.evaluate()
    i+=1