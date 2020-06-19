# This is our Fuel Tank class, it is used as an interface between the Chasis and the Drivetrain.
# If you notice, it has no clue that the Drivetrain exists, it doesn't care. This allows this same class
# to be used in a ATV, or a Boat, or Plane. It's good practice to write things with as little dependencies as possible.
class FuelTank:
    def __init__(self):
        # We have the max_level and the current level.
        self.max_level = 100
        self.level = 0

    def add_gas(self, amount):
        # This is the add_gas function and takes the paramter with the amount. We ensure that the it doesn't overflow by
        # adding the the amount with the current level and bailing if it would overflow.
        if ((amount + self.level) > self.max_level):
            assert("Tank overfill, too much gas")
            return
        self.level =+ amount

    def use_gas(self):
        # The use_gas function will run until the level is 0. It will then let the user know that it is out of gas.
        self.level -= 1
        if(self.level < 1):
            assert("CAR OUT OF GAS. ADD GAS OR CAR WILL STOP WORKING")
            return