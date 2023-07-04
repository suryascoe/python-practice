from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = self.get_highscore()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_highscore(self):
        with open("data.txt") as data:
            return int(data.read())

    def update_highscore(self, updated_score):
        with open("data.txt", mode='w') as data:
            data.write(f"{updated_score}")

