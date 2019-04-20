score = int(input("님의 점수를 말하세요"))

if score<0 or score > 100:
    print("잘못입력했습니다.")

elif score>=90 :
    print("A학점입니다")

elif score>=80 :
    print("B학점입니다")

elif score>=70 :
    print("C학점입니다")

elif score>=60 :
    print("D학점입니다")

else:
    print("F학점입니다.")
