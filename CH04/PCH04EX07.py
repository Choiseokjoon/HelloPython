color1 = input("색상 #1을 입력하세요")
color2 = input("색상 #2을 입력하세요")
color3 = input("색상 #3을 입력하세요")

import turtle 
t = turtle. Turtle()
t.shape('turtle')
t.speed(100)

t.fillcolor(color1)
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100,0)
t.down()
t.fillcolor(color2)
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200,0)
t.down()
t.fillcolor(color3)
t.begin_fill()
t.circle(50)
t.end_fill()

