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

    def speed_up(self, speed):
        self.brake.release()
        self.accelerator.push()
        self.engine.accelerate()
    
    def slow_down(self, speed):
        self.accelerator.release()
        self.brake.push()
        self.engine.brake()

    def __str__(self):
        return str(self.engine)