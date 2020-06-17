# DISCLAIMER: This file is heavily commented, as you go deeper in the code, there will be less 
# "explanation comments" as the topic will probably be covered in this file.
# This actually has way to many comments, and hinders readability. I might actually upload a 
# non commented version, so you can see the code un-defiled.

# This is the class that builds the car, it takes all the components we defined and gives us a functioning vehicle.

# First we import our dependencies

from Chasis import Create_Chasis
from Drivetrain import Create_Drivetrain, LEFT, RIGHT

# Think of this as how we interact with a factory that makes cars.
# Programming speak would call this a contrived example of a "Factory Method"
def Create_Default_Car():
    return Car()


# This is our Car Class
# Think of a class as a box you get when you buy something. 
# You open the box, it has a bunch of other things that go together.
# Example: TV Box, inside of it is a TV, a Remote, a Power Cord, a Unuseful guide that most people don't read...

# The car class has: A Chasis (which gives us most of our functionality that the user cares about), and a Drivetrain 
# (which does most of the heavy lifting) This might be close to what programmers 
# call a "Frontend" and a "Backend", respectively.
class Car:

    # Python uses a special method __init__(self) that is used when creating a version of this class, as seen in the Create_Default_Car 
    # function on line 10. We don't pass any parameters to this, but we could if we wanted.
    # It would look something like def __init__(self, parameter1, parameter2)
    # If that was the case then you would "Instantiate" the class like Car("Blue", "4WD")

    def __init__(self):
        # Now we assign the class variables/properties/attributes (they are called a lot of things, depending on the language)
        # In our TV example above this would be similar to:
        # def __init__(self):
        #   self.Remote = Remote_Item()
        #   self.TV = TV_Item()

        self.chasis = Create_Chasis()
        self.drivetrain = Create_Drivetrain()

        # We then reference these class variables and connect them to our exposed engine API.
        # TV Example could be something like this:
        #   self.TV.ir_receiver.add_remote(self.Remote)

        self.drivetrain.engine.connect_fuel_tank(self.chasis.body.fuel_tank)
        self.drivetrain.engine.connect_transmission(self.drivetrain.transmission)

    def turn_on(self):
        # This is what can be known as a "wrapper" function. Essentially we add in some useful information and just call the 
        # engine's start_engine function. We are "wrapping" the start_engine() function, and adding in our debug comments.
        print("Attempting to start car")
        self.drivetrain.engine.start_engine()

    def turn_off(self):
        # Another wrapping function. Security wise, these wrapper functions also provide the user with less information. 
        # If the function took a parameter, we could use this wrapper function to check the input before passing it to our engine.
        # We could also call other things, like checking to ensure the car is in park before turning it off.
        print("Killing the engine")
        self.drivetrain.engine.stop_engine()

    def accelerate(self, to_speed=60):
        # Here we wrap the tranmission's speed_up() function, which calls the engine's accelerate function.
        # This function takes in a parameter called "to_speed", we set a default incase the user calls it without passing it in.
        # See line 109 and 111 to look at this function call and the brake function call below.
        while(self.drivetrain.transmission.get_current_speed() < to_speed):
            self.drivetrain.speed_up(to_speed)

    def brake(self, to_speed=0):
        # Very similar to the accelerate function call defined above. Check the comments in that function for further information.
        while(self.drivetrain.transmission.get_current_speed() > to_speed):
            self.drivetrain.slow_down(to_speed)
    
    def shift(self):
        # You can implement this if you want
        # I will probably add this in later, but it will create more complexity in the code.
        pass

    def turn_left(self):
        # Here we call the steering_wheel's turn() function, and we pass it a value from the turn enum that we create 
        # in the Turn.py file. Please look at the Drivetrain/Turn.py file for more information.
        self.drivetrain.steering_wheel.turn(LEFT)

    def turn_right(self):
        # Here we call the steering_wheel's turn() function, and we pass it a value from the turn enum that we create 
        # in the Turn.py file. Please look at the Drivetrain/Turn.py file for more information.
        self.drivetrain.steering_wheel.turn(RIGHT)

    def __str__(self):
        # These __functionname__() functions in python are usually considered "builtins"
        # Here we override the string function and have it return statuses of multiple dependencies
        # This __str__ function is called whenever you call python's built in print() function.
        # Essentially it is calling print(item_to_print.__str__()) which is also what you get when you call str(item).
        return "{}\n{}".format(self.chasis, self.drivetrain)

if __name__ == "__main__":

    # Instantiate the car using our factory method on line 13
    car = Create_Default_Car()
    

    # I commented this out, since it prints a lot of output. It essentially just checks to ensure that the times when you make 4 turns, 
    # you end up facing the same direction. This is what is sometimes known as an "edge case", it might not happen, but it could.
    # Test turning
    #for x in range(0,10):
    #    print(car.turn_left())
    #for x in range(0, 10):
    #    print(car.turn_right())

    # This actually calls the __str__ function we overrided on line 88
    print(car)

    print("-----------")
    print("Adding Gas")
    car.chasis.body.fuel_tank.add_gas(99)

    print("buckle our seatbelt")
    car.chasis.body.chair.buckleSeatBelt()

    print("Lets connect the fuel tank to our gauge")
    car.chasis.body.instrumentpanel.gas.connect_fuel_tank(car.chasis.body.fuel_tank)

    print("Lets try to start the engine")
    car.turn_on()

    print("-----------")
    
    print(car)

    print("-----------")

    # Here we pass the accelerate function a value of 20, if we didn't it would default to the vale 60, set on line 61 above.
    car.accelerate(to_speed=20)
    print(car)

    # Here we don't pass a value to the function, and the default 0 value is used.
    car.brake()
    car.turn_off()
    print(car)