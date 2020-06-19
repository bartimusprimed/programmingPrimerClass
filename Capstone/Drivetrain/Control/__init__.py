# __init__.py's are kinda unique to python, they allow you to mark the things underneath them as modules.
# It's not very straight forward, as they were originally used in python2.7 and I believe they changed the way
# they work in python 3. Either way, we create our factory methods to instantiate the accelerator, brake, and steering wheel.

from .Accelerator import Accelerator
from .Brake import Brake
from .Steering import Steering, Turn


def Create_Accelerator():
    return Accelerator()

def Create_Brake():
    return Brake()

def Create_Steering_Wheel():
    return Steering()