from .Accelerator import Accelerator
from .Brake import Brake
from .Steering import Steering, Turn


def Create_Accelerator():
    return Accelerator()

def Create_Brake():
    return Brake()

def Create_Steering_Wheel():
    return Steering()