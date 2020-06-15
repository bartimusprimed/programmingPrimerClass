class InstrumentPanel:
    def __init__(self, gasGauge=None, speedometerGauge=None):
        self.gas = gasGauge    
        self.speedometer = speedometerGauge
    
    def linkGasGauge(self, gasGauge):
        self.gas = gasGauge

    def linkSpeedometer(self, speedometer):
        self.speedometer = speedometer

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

