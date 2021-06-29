x = "x"
while True:
    num = eval(input("숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : "))
    if num == x:
        print("종료합니다")
        break
    elif num % 2 != 0:
        print(f"{num}은 홀수 입니다.")
    elif num % 2 == 0:
        continue