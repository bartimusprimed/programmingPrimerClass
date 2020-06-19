# Lets use an enum, not talked about in the powerpoint, but here is a quick explaination
# Enums can be used when you want to provide users with specific choices.
# Think of them like a dropdown box you use on a website.
# They allow you to write code that limits the situations (state) that your program might encounter.
#  This is an enum that keeps track of what direction the car is facing

# Python needs a library import to make enums work
from enum import Enum


# We declare the enum with a class keywork while inheriting the Enum parent class.
class Direction(Enum):
    # Each constant (variable that doesn't change) is given an oridinal value (a fancy way of saying a number that is in a sequence)
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    # A function that returns the name and value
    def describe(self):
        return self.name, self.value
    # An override for the __str__ method.    
    def __str__(self):
        return 'Currently facing: {0}'.format(self.name)