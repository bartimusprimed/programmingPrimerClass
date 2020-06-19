# The gas gauge class, currently unused by the instrument panel, but written in a way that it doesn't care.
class Gas:
    def __init__(self, mpg=10, capacity=100):
        self.current_level = 0
        self.fuel_tank = None

    # Here we give it a fuel tank to connect to.
    def connect_fuel_tank(self, gas_tank):
        self.fuel_tank = gas_tank

    # We could call the attribute directly, but we want to be sure that a gas tank is connected.
    def get_current_gas_level(self):
        if self.fuel_tank is not None:
            self.current_level = self.fuel_tank.level
            return self.current_level
        else:
            return "Gas tank not connected"