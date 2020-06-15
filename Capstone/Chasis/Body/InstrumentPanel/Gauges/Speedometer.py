class Speedometer:
    
    def __init__(self, min_speed, max_speed):
        self.min = min_speed
        self.max = max_speed
        self.current = 0

    def increase_speed(self):
        if self.current <= self.max:
            self.current += 1

    def decrease_speed(self):
        if self.current > 0:
            self.current -= 1
