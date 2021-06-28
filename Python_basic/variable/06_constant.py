# 값이 변경되지 않는 값
# 파이썬에서는 별도의 상수가 없음
# 변수와 구분하기 위해 대문자로 사용할 뿐
# 나중에 상수의 값을 변경해도 오류 없음

PI = 3.141592
r = 10

area = PI * r * r

print(area)

#####################################

INT_RATE = 0.03
deposit = 10000
interest = deposit * INT_RATE
balance = deposit + interest

print(balance)
print(int(balance))
# 천단위 구분기호 사용
print(format(int(balance),',')) #format(출력값, 구분기호)

INT_RATE = "이자율"