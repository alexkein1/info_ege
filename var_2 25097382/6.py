from turtle import *
tracer(0)
m = 10
rt(90)
for i in range(7):
    rt(45)
    fd(11*m)
    rt(45)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(4, 'red')
update()
exitonclick()  # 115
