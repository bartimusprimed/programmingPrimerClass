class Accelerator:
    def __init__(self):
        self.pressed = False
    def push(self):
        self.pressed = True
    def release(self):
        self.pressed = False