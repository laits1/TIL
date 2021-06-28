#input ("프롬프트 문자열") => 입력되는 모든 값은 문자열로 반환
# x = int(input("숫자1 입력 :")) # 실수에서 에러
# y = float(input("숫자2입력 : "))
# z = eval(input("숫자 3입력 : "))
# print(x,y)

# print(z)
# print(type(z))

# 수식을 입력해도 수식의 계산값 변환을 진행함

a = eval(input("수식입력 : "))
print(a)
print(type(a))