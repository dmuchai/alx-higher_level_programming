#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a Square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x coordinate. Defaults to 0.
            y (int): The y coordinate. Defaults to 0.
            id (int): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, affecting both width and height."""
        self.width = value
        self.height = value
