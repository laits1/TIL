
def var_test(a):
    a = 7 # 지역변수 값을 변경하면 - 새로운 변수를 생성
    print(a, "메모리주소 : ", id(a))
    b = 10  # 지역변수
    print(b, "메모리주소 : ", id(b))

# 함수 외부
a = 10 
b = 'abc'
var_test(a)
print('전역변수 a', a, "메모리주소 : ", id(a))
print('전역변수 b', b, "메모리주소 : ", id(b))

# 매개 변수의 이름을 전역변수 이름과 같이 사용하지 말 것