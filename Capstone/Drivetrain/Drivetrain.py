from .Control import Create_Accelerator, Create_Brake, Create_Steering_Wheel
from .Engine import Create_Engine
from .Transmission import Create_Transmission

class Drivetrain:
    def __init__(self):
        # Build drivetrain requirements
        self.accelerator = Create_Accelerator()
        self.brake = Create_Brake()
        self.steering_wheel = Create_Steering_Wheel()
        self.engine = Create_Engine()
        self.transmission = Create_Transmission()