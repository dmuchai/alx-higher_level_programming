#!/usr/bin/python3
"""Describes Class Base"""
import json
import os
import csv
import turtle


class Base:
    """class will be the base of all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor to initialize the object.

        Args:
            id (int): The id for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries from a JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherit from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of list_objs to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y]
                            )
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file."""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj_data = {
                        'id': int(row[0]), 'width': int(row[1]),
                        'height': int(row[2]), 'x': int(row[3]),
                        'y': int(row[4])
                    }
                elif cls.__name__ == "Square":
                    obj_data = {
                        'id': int(row[0]), 'size': int(row[1]),
                        'x': int(row[2]), 'y': int(row[3])
                    }
                instances.append(cls.create(**obj_data))
        return instances

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of Rectangle or Square with attributes set.

        Args:
            **dictionary (dict): A dictionary of attribute values.

        Returns:
            An instance of Rectangle or Square with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.

        Returns:
            A list of instances of the class.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as file:
            json_data = file.read()

        list_dicts = cls.from_json_string(json_data)
        return [cls.create(**d) for d in list_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all Rectangles and Squares using the Turtle graphics module."""
        screen = turtle.Screen()
        screen.title("Rectangle and Square Drawings")
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.speed(2)
        t.pensize(2)

        def draw_shape(x, y, width, height, color="black"):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.color(color)
            t.begin_fill()
            for _ in range(2):
                t.forward(width)
                t.right(90)
                t.forward(height)
                t.right(90)
            t.end_fill()

        for rect in list_rectangles:
            draw_shape(rect.x, rect.y, rect.width, rect.height, color="blue")

        for square in list_squares:
            draw_shape(
                square.x,
                square.y,
                square.size,
                square.size,
                color="green"
            )

        turtle.done()
