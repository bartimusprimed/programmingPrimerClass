# Place holder
class Transmission:
    def __init__(self):
        self.current_speed = 0
        self.max_speed = 60
        self.is_parked = True
        self.engine_rpms = 0

    def speed(self, rpms):
        # for ease, we will set rpms divided by 100, to give us speed
        if (self.is_parked):
            print("Car is currently in park, shifting out of park")
            self.remove_park()
        self.current_speed = rpms/100
        print("currently traveling: {} MPH".format(self.current_speed))
        if(self.current_speed == 0):
            print("Car is not moving, vehicle being placed into park")
            self.is_parked = True

    def get_current_speed(self):
        print("currently traveling: {} MPH".format(self.current_speed))
        return self.current_speed

    def remove_park(self):
        self.is_parked = False
