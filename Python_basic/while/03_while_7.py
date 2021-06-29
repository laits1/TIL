# 사용자로부터 숫자를 입력받아 입력된 숫자가 7이면 종료 문자를 내보내고 프로그램 종료
# 7이 아니면 다시 입력을 받는다. (while)

num = int(input("처음 입력 : "))
while num != 7:
    num = int(input("다시 입력 : "))

print(f"{num}입력! 종료")