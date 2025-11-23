import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(10)
t.pencolor("green")
t.shape("turtle")

for _ in range(4):
    t.forward(50)
    t.right(90)



for _ in range(3):
    t.forward(100)
    t.left(120)

win.mainloop()