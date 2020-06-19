# This is our chasis class, it provides features to the user, this can be known as our "frontend".
# It essentially just holds everything physical the car has, including the Fuel Tank which is used by the 
# Drivetrain or "backend". So the Chasis' fuel tank "interfaces" with the backend.
from .Body import Create_Body

class Chasis:
    # We realy just create the body, I did this incase we wanted to add additional things to the chasis, like
    # wheels, shocks, etc... which wouldn't belong on the body.
    def __init__(self):
        self.body = Create_Body()

    # A string override that give useful information of all the connected objects.
    def __str__(self):
        return """
    Current Seat Status: \n
    \t Seat Color: {}\n
    \t Seatbelt is Buckled: {}\n
    Current Fuel Tank Status:\n
    \t Fuel Tank Level: {}\n
    Current Instrument Panel Status:\n
    \t Speedometer Status:\n
    \t\t Current Speed: {}\n
    \t Gas Gauge Status:\n
    \t\t Current Level: {}\n
    """.format(
            self.body.chair.color,
            self.body.chair.buckled,
            self.body.fuel_tank.level,
            self.body.instrumentpanel.speedometer.current,
            self.body.instrumentpanel.gas.get_current_gas_level()
        )

# We aren't using this right now, but python allows you to check if this module is being ran as itself.
# you can then define things to create if you used this module as a standalone.
if __name__ == "__main__":
    pass