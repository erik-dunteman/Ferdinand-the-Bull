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
    return actionspace

def get_action_from_actionspace(actionspace):
    maxindex = np.unravel_index(actionspace.argmax(), actionspace.shape)

    # Randomize the choice if multiple max values (such as when it is initialized with 0s)
    contenders = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if actionspace[maxindex[0]][maxindex[1]][maxindex[2]] == actionspace[i][j][k]:
                    # Then this argmax is a contender
                    contenders.append([i, j, k])
    rand_choice = random.randint(0,len(contenders)-1)
    print(len(contenders), "Possible Options")
    index_set = contenders[rand_choice]

    action = []
    for val in index_set:
        action.append(val-1)
    return action