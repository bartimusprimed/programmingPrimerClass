# This is our chair class, it has a color, a seatbelt, and tracks whether it has been buckled.

class Chair:
    def __init__(self, color="Black", seatbelt=True):
        # The default parameters set the color and seatbelt to True.
        self.color = color
        self.seatbelt = seatbelt
        self.buckled = False
    # We check if there is a seatbelt, and then buckle it.
    def buckleSeatBelt(self):
        if self.seatbelt:
            self.buckled = True
    
    # We check again if there is a seatbelt, and unbuckle it.
    def unbuckleSeatBelt(self):
        if self.seatbelt:
            if self.buckled:
                self.buckled = False
                
if __name__ == "__main__":
    pass