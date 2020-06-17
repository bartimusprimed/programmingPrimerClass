### This is the engine class, the only things referenced outside this class is the fuel_tank and transmission, which is needed to function properly. ###
### It can still be created by itself, but it will check to ensure those dependencies exist before attempting to use them ###

class Engine:
    def __init__(self):
        self.cylinder_count = 4
        self.max_rpm = 6000
        self.is_on = False
        self.current_rpm = 0
        self.fuel_tank = None
        self.transmission = None
        
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

    def start_engine(self):
        self.is_on = True

    def stop_engine(self):
        self.is_on = False

    def accelerate(self):
        if (self.fuel_tank is None or self.transmission is None):
            assert("Ensure you connected a fuel tank and transmission to the engine")
            return
        if (self.current_rpm < self.max_rpm):
            self.current_rpm += 100
            self.transmission.speed(self.current_rpm)
            self.use_fuel()

    def use_fuel(self):
        if (self.fuel_tank is None):
            assert("You have no fuel tank")
            return
        self.fuel_tank.use_gas()

    def brake(self):
        if (self.fuel_tank is None or self.transmission is None):
            assert("Ensure you connected a fuel tank and transmission to the engine")
        if (self.current_rpm > 0):
            self.current_rpm -= 100
            self.transmission.speed(self.current_rpm)

    def connect_fuel_tank(self, fuel_tank):
        self.fuel_tank = fuel_tank

    def connect_transmission(self, transmission):
        self.transmission = transmission