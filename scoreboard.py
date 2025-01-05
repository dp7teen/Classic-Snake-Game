from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 280)
        self.write("SCORE = " + str(self.score), align="center", font=('Arial', 15, 'normal'))

    def count_score(self):
        self.clear()
        self.score += 1
        self.goto(0, 280)
        self.write("SCORE = " + str(self.score), align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'bold'))