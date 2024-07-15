#!/usr/bin/python3
"""Module that creates a square class"""


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        """Calculates the area of the square."""
        return self.side ** 2

    def perimeter(self):
        """Calculates the perimeter of the square."""
        return self.side * 4

    def __str__(self):
        return f"Square with side length: {self.side}"

if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print(s.area())
    print(s.perimeter())
