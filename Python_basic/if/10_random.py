#가위바위보 데이터 받기
# 홍길동과 컴퓨터간의 가위바위보 게임

# 랜덤 모듈 가져오기

from random import randint
#난수 발생 : 1: 가위, 2:바위 , 3:보
n = randint(1,3)

if n == 1 :
    lee = "가위"
elif n == 2 :
    lee = "바위"
else :
    lee = "보"


hong = input("홍길동 입력 : ")
# 홍길동이 이기는 모든 경우의 수를 if 조건으로 생성
print(f"컴퓨터 이몽룡 입력 : {lee}")

if (hong == "가위" and lee == "보") \
        or (hong == "바위" and lee == "가위") \
        or (hong == "보" and lee == "바위"):
    print("홍길동이 이겼습니다.")
elif (hong == lee):
    print("비겼습니다.")
else:
    print("이몽룡이 이겼습니다.")