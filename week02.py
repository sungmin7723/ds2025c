import random

randomNum =  random.randint(1, 100)

win = False

for i in range(7, 0, -1) :
    print(f"{i}번 남았음")

    guessNum = int(input("숫자 입력 : "))

    if guessNum == randomNum :
        print("정답입니다")
        win = True
        break

    elif guessNum > randomNum :
        print("더 낮음.")

    elif guessNum < randomNum :
        print("더 높음.")

if win :
    print("you win")
else :
    print(f"정답 {randomNum}인데 이걸 못 맞추네 ㅋ 어휴 ㅉㅉ ㅄ 수준 ㅋ")
