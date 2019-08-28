from rl_utils import get_actionspace, get_action_from_actionspace

class Cow():
    def __init__(self):
        self.distance = 0 # How far the cow has moved forward. The reward function.
        self.right = 0 # Where right is the rotary position of the right leg. 
                        #Options: [-2, -1, 0, 1, 2] where 0 is neutral and 2 is full forward
        self.left = 0 # Where left is the rotary position of the left leg. 
                        #Options: [-2, -1, 0, 1, 2] where 0 is neutral and 2 is full forward
        self.hips = 0 # Where hips is the rotary position of the hips. 
                        #Options: [-1, 0, 1] where 0 is neutral and 1 is clockwise rotation, viewed from behind, causing cow to stand on right leg

    def get_action(self, qtable):
        action = [0,0,0] # Default action, where, respectively, the values indicate which direction to increment the right, left, and hips.

        right = self.right + 2 #Adjust index value from absolute leg position (-2 based) to 0 based
        left = self.left + 2
        hips = self.hips + 1   #Adjust index value from absolute hipposition (-1 based) to 0 based

        actionspace = get_actionspace(qtable, right, left, hips)
        action = get_action_from_actionspace(actionspace)
        return action

    def act(self, action):
        self.right += action[0]
        self.left += action[1]
        self.hips += action[2]
        
        #No correct for overrotation
        if self.right == 3: 
            self.right = 2
        if self.right == -3: 
            self.right = -2
        if self.left == 3: 
            self.left = 2
        if self.left == -3: 
            self.left = -2
        if self.hips == 2: 
            self.hips = 1
        if self.hips == -2: 
            self.hips = -1



    def evaluate(self):
        print()

