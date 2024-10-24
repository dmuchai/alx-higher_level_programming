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
        """Returns string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, affecting both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance.

        Args:
            *args (tuple): Non-keyword arguments in the order:
                1st: id, 2nd: size, 3rd: x, 4th: y.
            **kwargs (dict): Keyword arguments to update attributes.
        """
        if args and len(args) > 0:
            attr_names = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_names):
                    setattr(self, attr_names[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
