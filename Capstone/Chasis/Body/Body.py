from .Chair import Create_Chair
from .InstrumentPanel import Create_Instrument_Panel

class Body:
    def __init__(self):
        # Create the body and all functions needed
        self.chair = Create_Chair()
        self.instrumentpanel = Create_Instrument_Panel()