import random

com_num = random.randint(1,6)

user_num = int(input("주사위 숫자를 입력하세요 (1~6)"))

if com_num == user_num:
    print("어떻게 알았지? 운 한 번 드럽게 좋네요")

else:
    print("틀렸어 스거해 그럴 줄 알았다.")
    user_num = int(input("주사위 숫자를 입력하세요 (1~6)"))
    if com_num == user_num:
        print("어떻게 알았지? 운 한 번 드럽게 좋네요")

    else:
         print("틀렸어 스거해 그럴 줄 알았다.")
         user_num = int(input("주사위 숫자를 입력하세요 (1~6)"))
         if com_num == user_num:
            print("어떻게 알았지? 운 한 번 드럽게 좋네요")

         else:
            print("틀렸어 스거해 그럴 줄 알았다.")
        
    


