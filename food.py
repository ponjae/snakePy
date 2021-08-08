from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        """
        Initialize the class and the super class
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        """
        Method for generating a "food circle" on a random place in the window
        """
        random_x = randint(-280, 280)
        random_y = randint(-280, 265)
        self.goto(random_x, random_y)
