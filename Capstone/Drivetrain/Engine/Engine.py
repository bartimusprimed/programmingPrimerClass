# Placeholder
class Engine:
    def __init__(self):
        self.cylinder_count = 4
        self.max_rpm = 6000
        self.is_on = False
        self.current_rpm = 0
        self.fuel_tank = None
        self.transmission = None
        
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
        if(self.fuel_tank.level > 0):
            self.fuel_tank -= 1
        else:
            assert("Out of gas")

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