from turtle import Turtle
ALINMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.retrieve_high_score()
        self.update_score()

    def retrieve_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def update_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALINMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_high_score()
        self.retrieve_high_score()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
