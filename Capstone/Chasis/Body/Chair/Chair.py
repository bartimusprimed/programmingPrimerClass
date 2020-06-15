# This is called a factory method, it creates a chair for us.
class Chair:
    def __init__(self, color="Black", seatbelt=True):
        self.color = color
        self.seatbelt = seatbelt
        self.buckled = False

    def buckleSeatBelt(self):
        if self.seatbelt:
            self.buckled = True
    
    def unbuckleSeatBelt(self):
        if self.seatbelt:
            if self.buckled:
                self.buckled = False
                
if __name__ == "__main__":
    pass