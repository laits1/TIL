# 사용자로부터 점수를 입력받아서 학점을 구하는 프로그램

jumsu = eval(input("당신의 점수를 입력하세요 : "))

if jumsu >= 90:
    print(f'A')
elif jumsu >= 80:
    print(f'B')
elif jumsu >= 70:
    print(f'C')
elif jumsu >= 60:
    print(f'D')
else:
    print(f'F')