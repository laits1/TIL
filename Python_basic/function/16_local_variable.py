# 예제 함수 정의
def show():
    a = 1 # 함수 내에서 정의된 지역 변수
    a += 1
    print(a)    # 변수 a는 함수 내에서만 사용가능

def show1(b):
    b= b+1
    print(b)

show1(20) 
print(b)