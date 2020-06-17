from .Body import Create_Body

class Chasis:
    def __init__(self):
        self.body = Create_Body()

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

if __name__ == "__main__":
    pass