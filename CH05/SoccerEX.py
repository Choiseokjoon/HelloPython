#축구게임 기모띠

import random

position = ["가운데","오른쪽","왼쪽"]

com_pos = random.choice(position)
#print(com_pos)

user_pos = input("위치를 선택하세요(가운데/오른쪽/왼쪽)")

if com_pos == user_pos:
    print("노골입니다!!!! 스거하세요~~로로로로로롤")

else:
    print("아 ㅅㅂ...골이네...")

