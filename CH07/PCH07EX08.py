#add(a,b)
#sub(a,b)
#mul(a,b)
#sub(a,b)


a = int(input("첫 번째 수를 입력하시오."))
b = int(input("두 번째 수를 입력하시오"))
sym = input("사칙연산 중 하나를 입력하시오.")

if sym == + :
    print("(",a, "+",b,") =", a+b)
elif sym== "-":
    print("(",a, "-",b,") =", a-b)

elif sym == "*":
    print("(",a, "*",b,") =", a*b)

elif sym == "/":
    print("(",a, "/",b,") =", a/b)

