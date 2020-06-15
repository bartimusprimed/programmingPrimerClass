# This is the class that builds the car, it takes all the components we built and gives us a functioning vehicle.
from Chasis import Create_Chasis
from Drivetrain import Create_Drivetrain, LEFT, RIGHT

# A Factory Method to create a car
def Create_Default_Car():
    return Car()

class Car:

    def __init__(self):
        self.chasis = Create_Chasis()
        self.drivetrain = Create_Drivetrain()

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

    def turn_left(self):
        self.drivetrain.steering_wheel.turn(LEFT)

    def turn_right(self):
        self.drivetrain.steering_wheel.turn(RIGHT)


if __name__ == "__main__":
    car = Create_Default_Car()
    print(car)
    print(car.chasis.body.instrumentpanel.gas.capacity)
    print(car.chasis.body.chair.buckled)
    car.chasis.body.chair.buckleSeatBelt()
    print(car.chasis.body.chair.buckled)
    for x in range(0,10):
        print(car.turn_left())
    for x in range(0, 10):
        print(car.turn_right())
    print(car.drivetrain)