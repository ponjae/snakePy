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
        self.highscore = self._read_hs_file()
        self.color("white")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        """
        Method for updating the scoreboard shown on the screen
        """
        self.clear()
        self.write(f"Your current score: {self.score}, Highscore: {self.highscore}", align=ALIGNMENT,
                   font=FONT)

    def _read_hs_file(self):
        """
        Helper method for reading the highscore from the data file
        """
        with open("data.txt", "r") as file:
            hs = file.read()
            return int(hs)

    def _write_new_hs(self):
        """
        Helper method for writing the new highscore to data file
        """
        with open("data.txt", "w") as file:
            file.truncate(0)
            file.write(str(self.highscore))

    def reset(self):
        """
        Method for resetting the scoreboard and updating highscore if beaten
        """
        if self.score > self.highscore:
            self.highscore = self.score
            self._write_new_hs()
        self.clear()
        self.score = 0
        self.write(f"Your current score: {self.score}, Highscore: {self.highscore}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        """
        Increase the score
        """
        self.score += 1

    # def game_over(self):
    #     self.color("red")
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT,
    #                font=("Courier", 30, "bold"))
