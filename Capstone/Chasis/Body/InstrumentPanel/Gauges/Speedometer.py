# The speedometer gauge class, currently unused by the instrument panel, but written in a way that it doesn't care.
# it needs a connection to the engine, see if you can make it happen.
class Speedometer:
    
    def __init__(self, min_speed=0, max_speed=60):
        self.min = min_speed
        self.max = max_speed
        self.current = 0

    def increase_speed(self):
        if self.current <= self.max:
            self.current += 1

    def decrease_speed(self):
        if self.current > 0:
            self.current -= 1
