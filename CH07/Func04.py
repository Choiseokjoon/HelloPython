def sum_all(s):
    sum_result = 0
    for i in s:
        sum_result += i
    return sum_result

import random


a = [1,3,5,7]
sum_a = sum_all(a)
print("리스트의 합:" , sum_a)
b = []

for i in range(10):
    num = random.randint(1,100)
    b.append(num)
result = sum_all(b)
print("리스트의 합:" , result)

    
