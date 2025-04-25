import turtle
t=turtle.Turtle()
t.penup()
t.goto(10,20)
t.pendown()
for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
t.penup()
t.goto(75,1)
t.pendown()
for i in range(4):
    t.forward(50)
    t.right(90)
