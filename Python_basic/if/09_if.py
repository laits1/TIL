#가위바위보 데이터 받기
hong = input("홍길동 입력 : ")
lee = input("이몽룡 입력 : ")

# 홍길동이 이기는 모든 경우의 수를 if 조건으로 생성

if (hong == "가위" and lee == "보") \
        or (hong == "바위" and lee == "가위") \
        or (hong == "보" and lee == "바위"):
    print("홍길동이 이겼습니다.")
elif (hong == lee):
    print("비겼습니다.")
else:
    print("이몽룡이 이겼습니다.")