from turtle import Turtle, goto
import turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.points = 0
        self.pu()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 280)
        self.ht()
        self.write(f"Score = {self.points}", align = "center", font = ("Arial", 15, "normal"))


    def score(self):
        self.clear()
        self.points += 1
        self.write(f"Score = {self.points}", align = "center", font = ("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font = ("Arial", 15, "normal"))
