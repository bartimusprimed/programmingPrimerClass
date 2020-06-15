from enum import Enum

class Turn(Enum):
    LEFT = -1
    RIGHT = 1

    def describe(self):
        return self.name, self.value

def Turn_Left():
    return Turn.LEFT

def Turn_Right():
    return Turn.RIGHT