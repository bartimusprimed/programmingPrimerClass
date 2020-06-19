# Our Transmission class is quite simple, it tracks the current_speed, the max_speed, whether the vehicle is in park, and the engine's current rpms.
class Transmission:
    def __init__(self):
        self.current_speed = 0
        self.max_speed = 60
        self.is_parked = True
        self.engine_rpms = 0

    # This speed function takes an rpm parameter and sets the current speed equal to the rpm's divided by 100.
    def speed(self, rpms):
        # Is the car in park? if so, shift out of park.
        if (self.is_parked):
            print("Car is currently in park, shifting out of park")
            self.remove_park()
        # for ease, we will set rpms divided by 100, to give us speed
        self.current_speed = rpms/100
        print("currently traveling: {} MPH".format(self.current_speed))
        # Is the car's speed 0? If so, lets shift the vehicle into park.
        if(self.current_speed == 0):
            print("Car is not moving, vehicle being placed into park")
            self.is_parked = True

    def get_current_speed(self):
        # We could just call the transmission.current_speed attribute (aka class variable), but we create a nice wrapper function that formats a string for us.
        # Python does have attribute getter's and setter's, but they are a little more complicated to use.
        # Other languages have a different format for this, and they allow you to declare getters and setters when you declare the class variables.
        print("currently traveling: {} MPH".format(self.current_speed))
        return self.current_speed

    def remove_park(self):
        # Remove the parking brake.
        self.is_parked = False
