# __init__.py's are kinda unique to python, they allow you to mark the things underneath them as modules.
# It's not very straight forward, as they were originally used in python2.7 and I believe they changed the way
# they work in python 3. Either way, we create our factory method in here to instantiate the Chasis.
from .Chasis import Chasis
def Create_Chasis():
    return Chasis()