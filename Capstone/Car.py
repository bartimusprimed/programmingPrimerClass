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
        # These are using an exposed engine API to connect other parts of the car
        self.drivetrain.engine.connect_fuel_tank(self.chasis.body.fuel_tank)
        self.drivetrain.engine.connect_transmission(self.drivetrain.transmission)

    def turn_on(self):
        print("Attempting to start car")
        self.drivetrain.engine.start_engine()

    def turn_off(self):
        print("Killing the engine")
        self.drivetrain.engine.stop_engine()

    def accelerate(self, to_speed=60):
        while(self.drivetrain.transmission.get_current_speed() < to_speed):
            self.drivetrain.speed_up(to_speed)

    def brake(self, to_speed=0):
        while(self.drivetrain.transmission.get_current_speed() > to_speed):
            self.drivetrain.slow_down(to_speed)
    
    def shift(self):
        # You can implement this if you want
        pass

    def turn_left(self):
        self.drivetrain.steering_wheel.turn(LEFT)

    def turn_right(self):
        self.drivetrain.steering_wheel.turn(RIGHT)

    # Lets override the string function and have it return statuses of multiple exposed apis
    def __str__(self):
        return "{}\n{}".format(self.chasis, self.drivetrain)

if __name__ == "__main__":
    car = Create_Default_Car()
    
    # Test turning
    #for x in range(0,10):
    #    print(car.turn_left())
    #for x in range(0, 10):
    #    print(car.turn_right())

    print(car)
    print("\n\n-----------\n\n")
    print("Adding Gas")
    car.chasis.body.fuel_tank.add_gas(99)
    print("buckle our seatbelt")
    car.chasis.body.chair.buckleSeatBelt()
    print("Lets connect the fuel tank to our gauge")
    car.chasis.body.instrumentpanel.gas.connect_fuel_tank(car.chasis.body.fuel_tank)
    print("Lets try to start the engine")
    car.turn_on()
    print("\n\n-----------\n\n")
    print(car)

    print("\n\n-----------\n\n")
    car.accelerate(to_speed=20)
    print(car)
    car.brake()
    car.turn_off()
    print(car)