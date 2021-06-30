# 리스트 변수 복사

a = [1,2,3]
# 리스트 [1,2,3]을 메모리 어딘가 저장하고
# 저장되어있는 주소를 a가 가지고 있다.

# a 리스트의 값을 b 변수에 복사하시오.
# 참조값(주소) 복사, 얕은 복사
# 원본을 변경하면 복사본 내용도 변경
b = a


# a변수의 값을 b 변수에 저장하는 코드
print(a)
print(b)

b[0] = 100

print(a)
print(b)
#b[0] 원소 값을 변경했는데 a[0] 원소값도 변경


# 깊은복사
# list() 함수 또는 deepcopy() 함수 사용

scores = [1,2,3,4,5]
values = list(scores)

print(scores)
print(values)

values[0] = 100
print()
print(scores)
print(values)

# deepcopy() 함수 : 깊은 복사
# copy 모듈을 import 해야함

import copy
a=['a','b','c']
b = copy.deepcopy(a)

print("b리스트 수정 전")
print(a)
print(b)

b[0] = 1    
print("b 리스트 수정 후")
print(a)
print(b)
