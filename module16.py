import turtle
turtle.setup(960,720,0,500)

def circ(x):
    if x > 200:
        return
    turtle.circle(x,steps=100)
    turtle.left(5)
    print(x)
    circ(x + 1)

turtle.tracer(5,0)
turtle.shape("turtle")
turtle.shapesize(1,1,1.5)
turtle.pencolor(0,0.6,0)
turtle.fillcolor(0,1,0)
turtle.begin_fill()
circ(1)
turtle.end_fill()
turtle.mainloop()