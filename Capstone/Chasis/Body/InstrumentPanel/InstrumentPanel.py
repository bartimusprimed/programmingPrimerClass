class InstrumentPanel:
    def __init__(self, numberOfGauges=2):
        if numberOfGauges == 2:
            self.gas = 100
            self.speed = 0
        else:
            self.speed = 0
            # Gas gauge isn't needed, just ask my 1982 nissan datsun
            self.gas = None

    def accelerate(self):
        pass

    def brake(self):
        pass

    