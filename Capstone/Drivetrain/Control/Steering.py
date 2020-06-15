# Lets use an enum, not talked about in the powerpoint, but we will explain it in the class
from enum import Enum
from ..Turn import Turn
from ..Direction import Direction

class Steering:

    def __init__(self,  initial_direction=Direction.NORTH):
        self.current_direction = initial_direction
        self.turn_options = Turn
        # Center will be 0, left will be -90 and right will be 90

    # We can use the __str__ method overwrite to make a default print statement
    def __str__(self):
        return "Car is currently facing {0}".format(Direction(self.current_direction).describe())

    def turn(self, direction):
        # Handle turning edge condition right
        print("Turning {0}".format(direction))
        if direction == Turn.RIGHT and self.current_direction == Direction.WEST:
            self.current_direction = Direction(0)
        # Handle turning edge condition left
        elif direction == Turn.LEFT and self.current_direction == Direction.NORTH:
            self.current_direction = Direction(3)
        else:
            self.current_direction = Direction(self.current_direction.value + direction.value)
        return self.current_direction

if __name__ == "__main__":
    # Test Cases
    steering_wheel = Steering()
    # print(steering_wheel.current_direction) <- we would use this normally, but since we overwrote the __str__ method we can just call print on the object
    # Check turn reset
    for x in range(0, 6):
        steering_wheel.turn(Turn.LEFT)
        print(steering_wheel)
    for x in range(0, 6):
        steering_wheel.turn(Turn.RIGHT)
        print(steering_wheel)