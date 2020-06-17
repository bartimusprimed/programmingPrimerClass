# Lets use an enum, not talked about in the powerpoint, but we here is a quick explaination
# Enums can be used when you want to provide users with specific choices.
# Think of them like a dropdown box you use on a website.
# They allow you to write code that limits the situations (state) that your program might encounter.
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