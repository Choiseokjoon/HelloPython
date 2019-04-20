x1 = int(input("첫 번째 점의 x좌표를 입력하세요"))
y1 = int(input("첫 번째 점의 y좌표를 입력하세요"))
x2 = int(input("두 번째 점의 x좌표를 입력하세요"))
y2 = int(input("두 번째 점의 y좌표를 입력하세요"))

distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(distance)
