### This is the engine class, the only things referenced outside this class is the fuel_tank and transmission, which is needed to function properly. 
###
### It can still be created by itself, but it will check to ensure those dependencies exist before attempting to use them ###

class Engine:
    # Here we set some class variables that aren't used yet. They are there if we plan on extending the functionality or features of the engine.
    # We set a limit on the max_rpm, which is provided to the transmission to increase the speed of the car.
    # The fuel tank and the transmission are set to None, which is sometimes called "null", "nil", "empty", etc... in other languages.

    def __init__(self):
        self.cylinder_count = 4
        self.max_rpm = 6000
        self.is_on = False
        self.current_rpm = 0
        self.fuel_tank = None
        self.transmission = None

    # Here we override the string and do a check to see if the engine is running or not, we then take that and add it to another string
    # that prints out additional information. This is called string interpolation, it essentially just means including variables in the string
    # that change during runtime. This is sometimes called a "format string" in other languages, you assign place holders in the original
    # string and they get replaced when the string is returned.     
    def __str__(self):
        engine_status = "off"
        if self.is_on:
            engine_status = "running"

        return "Engine Cylinder Count {}, Engine is currently {}, Engine current RPMS: {}, Engine Fuel Level {}, Engine Speed {}".format(
                self.cylinder_count,
                engine_status,
                self.current_rpm,
                self.fuel_tank.level,
                self.transmission.current_speed
            )

    # Simple.
    def start_engine(self):
        self.is_on = True
    # Simple
    def stop_engine(self):
        self.is_on = False

    # Here we tell the engine to accelerate. First it checks to ensure that a fuel tank and a transmission has been connected to it.
    # Then it ensure that it's rpms are under, the max limit. If it is passes the new rpms to the transmission, and runs the use fuel
    # function that is declared below.
    def accelerate(self):
        if (self.fuel_tank is None or self.transmission is None):
            assert("Ensure you connected a fuel tank and transmission to the engine")
            return
        if (self.current_rpm < self.max_rpm):
            self.current_rpm += 100
            self.transmission.speed(self.current_rpm)
            self.use_fuel()
    # This just call's the fuel tank's use_gas method (just another name for a function that belongs to a class, they are often used interchangeably)
    # We could had just called this directly above, but I wanted to show different use cases.
    def use_fuel(self):
        if (self.fuel_tank is None):
            assert("You have no fuel tank")
            return
        self.fuel_tank.use_gas()
    # Similar to the accelerate method, we check for fuel_tank and transmission and then make changes.
    # Side note: Python is a relatively safe language, and will often forgive you for attempting to 
    # use things that haven't been initialized. Technically since the car could not get to the brake
    # state without hitting the accelerate state, this is kind of unnecessary. We are checking again,
    # just to be sure since we don't want to reference something that is set to none.
    # In C,  or other lower languages this leads to what is called a "null pointer" (dereference)
    # You essentially attempt to read a value that has been cleared or not initialized to a value,
    # if this check wasn't here, a malicious user could look and see if there was anything stopping
    # them from removing the fuel_tank or transmission during run and cause the program to print/change/modify something store in it's place.
    def brake(self):
        if (self.fuel_tank is None or self.transmission is None):
            assert("Ensure you connected a fuel tank and transmission to the engine")
        if (self.current_rpm > 0):
            self.current_rpm -= 100
            self.transmission.speed(self.current_rpm)

    # Here we connect a fuel tank.
    def connect_fuel_tank(self, fuel_tank):
        self.fuel_tank = fuel_tank
    # Here we connect a transmission.
    def connect_transmission(self, transmission):
        self.transmission = transmission