import turtle
import random
scn=turtle.Screen()
i = random.randint(5,20)
colors = ["plum", "SpringGreen", "DeepSkyBlue", "Maroon", ]



class ShapeFactory():
    def __init__(self):
        self.t=turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(300)
        self.t.pu()
        self.x = random.randint(-640, 480)
        self.y = random.randint(-640, 480)
        self.t.goto(self.x, self.y)
        self.t.pd()

    def triangle(self):
        self.t.fillcolor(random.choice(colors))
        self.t.begin_fill()
        mp = random.randint(20,50)
        for n in range(0, 3, 1):
            self.t.fd(mp)
            self.t.rt(120)
        self.t.end_fill()


    def rectangle(self):
        tt = random.randint(20,100)
        self.t.fillcolor(random.choice(colors))
        self.t.begin_fill()
        for m in range(0, 4, 1):
            self.t.fd(tt)
            self.t.rt(90)
        self.t.end_fill()

    def circle(self):
        r = random.randint(20, 50)
        self.t.fillcolor(random.choice(colors))
        self.t.begin_fill()
        self.t.circle(r)
        self.t.end_fill()



for i in range(0,100):
    nikolas=ShapeFactory()
    shape=random.randint(1,3)

    if shape==1:
        nikolas.triangle()
    elif shape==2:
        nikolas.rectangle()
    elif shape==3:
        nikolas.circle()