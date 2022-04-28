#!/usr/bin/python3
"""A Base class"""
import json
import csv
import turtle as t


class Base:
    """A class representing a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method constructs an instance of the Base class
        Args:
            id (any)
        """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a python dictionary to JSON string
        Args:
            list_dictionaries (list)
        Returns: A JSON string representation of list_dictionaries

        """
        if list_dictionaries is None or len(list_dictionaries) == 0\
                or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method writes the JSON string representation of
        list_objs to a file
        Args:
            list_objs (list)

        """
        mylist = []
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as jfile:
            if list_objs is None or len(list_objs) == 0 or list_objs == []:
                jfile.write("[]")
            else:
                for obj in list_objs:
                    mylist.append(cls.to_dictionary(obj))
                jfile.write(cls.to_json_string(mylist))

    @staticmethod
    def from_json_string(json_string):
        """Method converts a json string to python object and returns it
        Args:
            json_string (str)
        Returns: A python object

        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method returns an instance with all attributes set
        Args: dictionary (dict)

        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 2)
            if cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Method returns a list instances of object"""
        my_list = []
        try:
            with open(str(cls.__name__) + ".json", "r") as f:
                my_dict = cls.from_json_string(f.read())
                for k in my_dict:
                    my_list.append(cls.create(**k))
                return my_list
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method serializes in CSV
        Args:
            list_objs (list) list of arguments supplied to the function

        """
        with open(cls.__name__ + ".csv", "w", newline="") as csvfile:
            if list_objs is None or list_objs == [] or len(list_objs) == 0:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Method deserializes a csv file
        """
        my_objs = []
        try:
            with open(cls.__name__ + ".csv", "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                for lines in reader:
                    if cls.__name__ == "Rectangle":
                        fields = {"id": int(lines[0]),
                                  "width": int(lines[1]),
                                  "height": int(lines[2]),
                                  "x": int(lines[3]),
                                  "y": int(lines[4])
                                  }
                    if cls.__name__ == "Square":
                        fields = {"id": int(lines[0]),
                                  "size": int(lines[1]),
                                  "x": int(lines[2]),
                                  "y": int(lines[3])
                                  }
                    my_objs.append(cls.create(**fields))
                return my_objs
        except IOError:
            return []

    @staticmethod
    def create_rectangle(rect):
        """Method creates a rectangle by turtle
        Args:
            rect (Rectangle)
        """
        t.pendown()
        for counter in range(2):
            t.forward(rect.width)
            t.right(90)
            t.forward(rect.height)
            t.right(90)
        t.penup()
        t.hideturtle()

    @staticmethod
    def create_square(sq):
        """Method creates a Square by turtle
        Args:
            sq (Square)
        """
        t.pendown()
        for counter in range(2):
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
        t.penup()
        t.hideturtle()

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Method opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): list of Rectangle instances
            list_squares (list): list of Square instances
        """
        xpos = -250
        ypos = 50

        t.bgcolor('Dodger blue')
        t.pensize(2)
        t.color('blue')
        t.shape('turtle')
        t.setheading(0)
        t.showturtle()
        t.penup()

        for rect in list_rectangles:
            t.goto(xpos, ypos)
            Base.create_rectangle(rect)
            xpos = xpos + rect.width + 10

        xpos = -300
        ypos = 250
        for sq in list_squares:
            t.goto(xpos, ypos)
            Base.create_square(sq)
            xpos = xpos + sq.size + 10

        t.exitonclick()
