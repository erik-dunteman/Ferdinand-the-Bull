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
        # print("Action done been gotten.")

        right = self.right + 2 #Adjust index value from absolute leg position (-2 based) to 0 based
        left = self.left + 2
        hips = self.hips + 1   #Adjust index value from absolute hipposition (-1 based) to 0 based

        actionspace = get_actionspace(qtable, right, left, hips)
        action = get_action_from_actionspace(actionspace)
        return action

    def act(self, action):
        print()
        print("Right moving: ", action[0])
        print("Left moving: ", action[1])
        print("Hips moving: ", action[2])

    def evaluate(self):
        print("Ah yes, Ferdinand is satisfied with his personal self evaluation.")

