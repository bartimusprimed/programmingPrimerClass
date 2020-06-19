# Here we import our gauges, I commented this out, because right now we have not connected the 
# instrument panels to the engine. In the class, this should be an exercise to add this functionality. 
# You will have to find a way to interface between the transmission and the speedometer. You also should 
# find a way to interface the gas gauge with the fuel tank. You will need to "lift" or "wrap" the functionality. 
# Notice how I have functions in here, but those aren't the names of the functions in the actual classes. 
# Uncommenting these will break it. The program currently bypasses this class and directly interfaces with
# the gas gauge and speedometer.
from .Gauges import Create_Gauge_Gas, Create_Gauge_Speedometer

class InstrumentPanel:
    def __init__(self):
        self.gas = Create_Gauge_Gas()   
        self.speedometer = Create_Gauge_Speedometer()

    # def accelerate(self):
    #     self.speedometer.accelerate()
    #     self.gas.decrease()

    # def brake(self):
    #     self.speedometer.decelerate()

    # def fillGas(self, amount):
    #     if self.gas:
    #         self.gas.increase(amount)

    # def useGas(self):
    #     if self.gas:
    #         self.gas.decrease()

