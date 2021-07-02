# 전역 변수 (global variable)
# 함수 외부에서 정의된 변수
# 프로그램 내 모든 곳에서 사용 가능
# 함수 내에서 전역 변수의 값을 변경하려면 global 키워드 사용

a = 1
b = 2

def show():
    global c
    c=a+b
    print(a)
    print(b)
    print(c)

def add():
    print(a)

show()
add()
print(a)    # 전역변수는 모든 곳에서 사용 가능
print(b)     # 함수 내부/ 외부 모든 곳에서 전역변수 사용 가능
print(c)