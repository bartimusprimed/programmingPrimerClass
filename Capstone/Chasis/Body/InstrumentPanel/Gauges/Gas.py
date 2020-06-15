class Gas:
    def __init__(self, mpg=10, capacity=100):
        self.mpg = mpg
        self.capacity = capacity
        self.currentLevel = 0
        self.decrease_amount = round(capacity/mpg)
        self.increase_amount = 1

    def increase(self, amount):
        self.currentLevel += amount

    def decrease(self):
        self.currentLevel -= self.decrease_amount