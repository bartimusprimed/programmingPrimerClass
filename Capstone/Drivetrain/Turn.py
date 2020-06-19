# Lets use an enum, not talked about in the powerpoint, but here is a quick explaination
# Enums can be used when you want to provide users with specific choices.
# Think of them like a dropdown box you use on a website.
# They allow you to write code that limits the situations (state) that your program might encounter.

# Import python's standard library dependency
from enum import Enum

# This is a simple Turn enum, we assigned the ordinals -1, and 1 to the Left and Rgiht Values.
class Turn(Enum):
    LEFT = -1
    RIGHT = 1

    def describe(self):
        return self.name, self.value

# This function is here strictly to provide access to the Turn.LEFT enumeration (enum).
def Turn_Left():
    return Turn.LEFT

# This function is here strictly to provide access to the Turn.RIGHT enumeration (enum).
def Turn_Right():
    return Turn.RIGHT