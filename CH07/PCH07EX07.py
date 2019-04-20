def circleArea(radius):
    area = PI * radius**2
    print("반지름이:", radius, "인 원의 면적은", area)
    
    return area

def circleCircumference(radius):
    area = 2* PI * radius
    print("반지름이:", radius, "인 원의 둘레은", area)

PI = 3.14
circleArea(5)
circleCircumference(5)
