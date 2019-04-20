
n = int(input("몇각형을 만들고 싶으신가요? (3 이상)"))
angle = 360/n

import turtle 
t = turtle. Turtle()
t.shape('turtle')
t.speed(15)

if n>= 10:
    for i in range(n):
        t.forward(25)
        t.left(angle)

else:
    for i in range(n):
        t.forward(100)
        t.left(angle)
