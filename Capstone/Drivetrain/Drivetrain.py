# This is our drivetrain class, it imports components that are needed to make and control the movement of the vehicle.
# All we are doing is encapsulating the other classes, and passing information between each other.

from .Control import Create_Accelerator, Create_Brake, Create_Steering_Wheel
from .Engine import Create_Engine
from .Transmission import Create_Transmission

class Drivetrain:
    # Most of the class variables are self explainatory.
    def __init__(self):
        # Build drivetrain requirements
        self.accelerator = Create_Accelerator()
        self.brake = Create_Brake()
        self.steering_wheel = Create_Steering_Wheel()
        self.engine = Create_Engine()
        self.transmission = Create_Transmission()

    # Here we have a speed_up function which is called by the main Car.py class, it submits a speed parameter.
    # We then ensure that the brake is released, we push the accelerator down, and let the engine know it should accelerate.
    def speed_up(self, speed):
        self.brake.release()
        self.accelerator.push()
        self.engine.accelerate()
    
    # Same as the speed_up function above except opposite.
    # We release the accelerator, push the brake down, and notify the engine that it should be braking.
    def slow_down(self, speed):
        self.accelerator.release()
        self.brake.push()
        self.engine.brake()

    # This is the override for the string method, We really only care about the engine, so we wrap the engine's str method and pass it along.
    # None of these objects are strictly dependent on one another, as we don't really care what the other components are doing.
    def __str__(self):
        return str(self.engine)