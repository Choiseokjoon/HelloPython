x1 = int(input("첫 번째 x좌표를  입력하세요"))
y1 = int(input("첫 번째 y좌표를  입력하세요"))

x2 = int(input("첫 번째 x좌표를  입력하세요"))
y2 = int(input("첫 번째 y좌표를  입력하세요"))



distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5


import turtle 
t = turtle. Turtle()
t.shape('turtle')

t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)

t.write(distance)
