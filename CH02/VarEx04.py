import turtle 
t = turtle. Turtle()
t.shape('turtle')
distance = int(input("집의 크기는 얼마로 할까요?"))

angle3 = 120
angle4 = 90

t.speed(100)
t.fd(distance)
t.left(angle4)
t.fd(distance)
t.left(angle4)
t.fd(distance)
t.left(angle4)
t.fd(distance)
t.left(angle4)
t.goto(0,100)
t.fd(distance)
t.left(angle3)
t.fd(distance)
t.left(angle3)
t.fd(distance)
t.left(angle3)

