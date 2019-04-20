x1 = int(input("x좌표 입력하세요"))
y1 = int(input("y좌표 입력하세요"))

x2 = int(input("x좌표 입력하세요"))

y2 = int(input("y좌표 입력하세요"))

x3 = int(input("x좌표 입력하세요"))

y3 = int(input("y좌표 입력하세요"))

list = [x1, y1, x2, y2, x3, y3]

import turtle 
t = turtle. Turtle()
t.shape('turtle')
t.speed(100)


t.goto(list[0],list[1])
t.goto(list[2],list[3])
t.goto(list[4],list[5])
