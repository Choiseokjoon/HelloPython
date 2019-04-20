user_input = int(input("숫자를 입력하세요(10~99)"))
user_s = str(user_input)


import random
lotto_num = random.randint(10,99)
lotto_s = str(lotto_num)
print(lotto_num)


if lotto_num == user_input:
    print("100만원 !!오 이런 어서 돈을 챙겨 이 나라를 떠나세요")
          
elif (user_s[0] == lotto_s[0]) or (user_s[0] == lotto_s[1]) or (user_s[1] == lotto_s[0]) or (user_s[1] == lotto_s[1]):
    print("50만원")

else :
    print("오... 이런 당첨되지 않으셨습니다.")




#elif (lotto_num // 10 == user_input//10) or (lotto_num % 10 == user_input% 10):
