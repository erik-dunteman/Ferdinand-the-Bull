import math
import numpy as np
import random
import datetime

def init_Qtable():

        '''Considering Statespace: Rotational position
            Right: [-2, -1, 0, 1, 2]    
            Left: [-2, -1, 0, 1, 2]  
            Hips: [-1, 0, 1]  

            Considering Actionspace: Direction to rotate
            Right: [-1, 0, 1]   
            Left: [-1, 0, 1]
            Hips: [-1, 0, 1]
        '''
        qtable = np.zeros([5,5,3,   3,3,3])

        return qtable

def get_actionspace(qtable, right, left, hips):
    actionspace = qtable[right][left][hips]
    actionspace[2][1][0] = 10
    return actionspace

def get_action_from_actionspace(actionspace):
    maxindex = np.unravel_index(actionspace.argmax(), actionspace.shape)
    action = []
    for val in maxindex:
        action.append(val-1)
    return action

