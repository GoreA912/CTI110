import turtle
win = turtle.Screen()
AG = turtle.Turtle()
AG.color("green")
AG.pensize(10)

def draw_A(t):
    t.pendown()
    t.left(70)
    t.forward(100)
    t.right(150)
    t.forward(100)
    t.backward(50)
    t.right(105)
    t.forward(30)
    t.penup()

def draw_G(t):
    t.pendown
    t.circle(50, 280)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.penup()

AG.penup()
AG.goto(-150, -50)
draw_A(AG)

AG.penup()
AG.goto(50, 50)
AG.pendown()
draw_G(AG)

win.mainloop()