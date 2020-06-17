from .Gauges import Create_Gauge_Gas, Create_Gauge_Speedometer

class InstrumentPanel:
    def __init__(self):
        self.gas = Create_Gauge_Gas()   
        self.speedometer = Create_Gauge_Speedometer()

    def accelerate(self):
        self.speedometer.accelerate()
        self.gas.decrease()

    def brake(self):
        self.speedometer.decelerate()

    def fillGas(self, amount):
        if self.gas:
            self.gas.increase(amount)

    def useGas(self):
        if self.gas:
            self.gas.decrease()

