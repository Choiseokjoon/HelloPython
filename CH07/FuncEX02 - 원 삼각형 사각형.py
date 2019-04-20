def circle_area():
    area = radius**2 * 3.14
    return area


def rect_area(side, height=50):
    area = side*height
    return area

def tri_area(side,height):
    area = side * height / 2
    return area

#radius = int(input("반지름:"))
#area0 = circle_area()
#print("원의 면적:",area0)

area0 = circle_area(10)
print("원의 넒이:", area0)

area4 = rect_area(10,20)
print("사각형의 넓이:" , area4)

area3 = tri_area(height = 10 , side = 20)
print("삼각형의 넓이:", area3)

rect44 = rect_area(10)
print("사각형의 넓이:", rect44)


