#!/usr/bin/python3
"""A class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """A class to represent a rectangle, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate. Default is 0.
            y (int): The y coordinate. Default is 0.
            id (int): The id. If not provided, it will be managed by Base.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangele
        Args:
            value (int): width of rectangle

        Raises:
            TypeError: if not integer
            ValueError: if value negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height

        Returns:
            int: rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter of rectangle height

        Args:
            value (int): rectangle height

        Raises:
            TypeError: if not integer
            ValueError: if negative value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x retriever

        Returns:
                int: x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x

        Args:
            value (int): x

        Raises:
            TypeError: if not integer
            ValueError: if negative non-integer
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y retriever

        Returns:
            int: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for y

        Args:
            value (int): y.

        Raises:
            TypeError: if not integer
            ValueError: if if negative non-integer
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the `#` character."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle's attributes."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
