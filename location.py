from turtle import Turtle
FONT = ("Arial", 10, "normal")

class Location(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.hideturtle()


    def go_to(self, x, y, state_name):
        self.goto(x, y)
        self.write(arg= state_name, align="center", font=FONT)