#dan = int(input("원하는 단을 입력하세요"))


for dan in range(2,10):
    for n in range(1,10):
        print(dan,"*",n, '=', dan*n, end="\t")
    print()
