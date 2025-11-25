from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 18, "normal")
SCORE_POSITION = (0, 270)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION[0], SCORE_POSITION[1])
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score is: {self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


