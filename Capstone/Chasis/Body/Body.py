# this is the body class, it contains our Chair, Instrument Panel, and Fuel Tank, technically the fuel tank could be moved up to the chassis class.
# I left this here as an exercise, to show the class how easy it is to move these things around, since we built it in a very modular way.
from .Chair import Create_Chair
from .InstrumentPanel import Create_Instrument_Panel
from .FuelTank import Create_Fuel_Tank

class Body:
    def __init__(self):
        # Create the body, which holds the chair, instrument panel, and fuel tank.
        self.chair = Create_Chair()
        self.instrumentpanel = Create_Instrument_Panel()
        self.fuel_tank = Create_Fuel_Tank()