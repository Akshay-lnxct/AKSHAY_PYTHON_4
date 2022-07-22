import turtle as t

t.speed(100)

for i in range(6):
    t.forward(150)
    t.backward(150)
    t.right(60)

side = 50

t.fillcolor("orange")

t.begin_fill()

for i in range(15):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)
    t.forward(side)
    t.right(120)

    for j in range(6):
        t.forward(side-2)
        t.right(60)
    side = side - 10

t.end_fill()
turtle.done()