class FuelTank:
    def __init__(self):
        self.max_level = 100
        self.level = 0

    def add_gas(self, amount):
        if ((amount + self.level) > self.max_level):
            assert("Tank overfill, too much gas")
            return
        self.level =+ amount

    def use_gas(self):
        self.level -= 1
        if(self.level < 1):
            assert("CAR OUT OF GAS. ADD GAS OR CAR WILL STOP WORKING")
            return