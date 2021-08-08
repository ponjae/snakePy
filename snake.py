from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """
        Initialize the class with segments and snakes
        """
        self.segments = []
        self._create_init_snakes()
        self.head = self.segments[0]

    def _create_init_snakes(self):
        """
        Helper method for creating the first three "snake blocks"
        """
        for position in STARTING_POSITIONS:
            self._add_segment(position)

    def _add_segment(self, pos):
        """
        Helper method for extending the body
        """
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        """
        Add segment to snake when successfully eating an orange
        """
        self._add_segment(self.segments[-1].position())

    def move(self):
        """
        Move each segment to the previous segments position, apart from the head.
        """
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Make the snake turn up
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Make the snake turn down
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Make the snake turn left
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Make the snake turn up
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
