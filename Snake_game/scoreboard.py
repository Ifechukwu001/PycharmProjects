from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 12, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}  HIGHSCORE: {self.high_score}", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1

    def remove_score(self):
        self.score -= 1

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(x=0, y=280)
        self.show_score()