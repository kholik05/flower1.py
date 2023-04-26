import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('#008000')
t.pencolor('#ffff00')
t.speed(100)
col = ('#ffC0CB', '#000000', '#800000', '#0000ff')

for n in range(5):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()
