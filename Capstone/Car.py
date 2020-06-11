class Car:

    def __init__(self, chasis=None, drivetrain=None):
        self.chasis = chasis
        self.drivetrain = drivetrain

    def turnOn(self):
        # Check Key
        # Check Brake
        # Fire Engine
        pass

    def turnOff(self):
        # Kill Engine
        pass

    def accelerate(self):
        # Check On
        # Check Brake
        # Check Fuel
        # Increase Engine RPM
        pass

    def brake(self):
        # Check Moving
        # Decrease Engine RPM
        pass
    
    def shift(self):
        # You can implement this if you want
        pass


if __name__ == "__main__":
    car = Car()