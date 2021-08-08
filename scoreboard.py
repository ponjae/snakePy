from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Helvetica", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """
        Initialize the scoreboard
        """
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        """
        Method for updating the scoreboard shown on the screen
        """
        self.clear()
        self.score += 1
        self.write(f"Your current score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT,
                   font=("Courier", 30, "bold"))
