from .Chair import Create_Chair
from .InstrumentPanel import Create_Instrument_Panel
from .FuelTank import Create_Fuel_Tank

class Body:
    def __init__(self):
        # Create the body and all functions needed
        self.chair = Create_Chair()
        self.instrumentpanel = Create_Instrument_Panel()
        self.fuel_tank = Create_Fuel_Tank()