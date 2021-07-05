
# 전역변수를 함수 내부에서 변경하려면? global 키워드 사용

a = 1 # 함수 밖에서 정의된 전역변수 a

def add():
    c=a+b
    print(a)
    print(b)
    print(c)

global b
b = 3   # 함수 밖에서 정의도니 전역변수 b

add()