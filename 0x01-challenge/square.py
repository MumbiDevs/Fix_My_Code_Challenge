#!/usr/bin/python3
"""Module that creates a square class"""

class Square:
    """Creates Square class"""

    def __init__(self, side=0):
        """init method that initializes attributes"""
        self.side = side

    def area(self):
        """Calculate the area of the square"""
        return self.side ** 2

    def perimeter(self):
        """Calculate the perimeter of the square"""
        return 4 * self.side

    def __str__(self):
        return "Square with side length: {}".format(self.side)

if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
