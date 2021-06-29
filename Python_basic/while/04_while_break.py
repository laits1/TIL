# 무한반복 예제
# 조건을 True로 만들고 계속 반복
# 반복문을 종료하기 위해 break 문을 사용

while True: # 조건이 무조건 참
    print("반복되는 문장입니다.")
    answer = input("종료하려면 x 입력 : ")
    if answer == 'x':
        break # 전체 반복 탈출

print("종료했습니다.")