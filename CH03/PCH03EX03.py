number = int(input("정수를 입력하세요"))

sum1000 = number//1000

sum100 = (number%1000) // 100

sum10 = (number%100) // 10

sum1 = (number%10) // 1

sum_all = (sum1000 + sum100 + sum10 + sum1)

print(sum_all)


