# while 문 : 조건식이 만족하는 동안 반복을 수행
# 반복의 횟수가 결정되어지지 않았을 때 주로 사용

# 초기 값 - 초기값이 없으면 조건 확인이 불가능(생략가능)
# while 조건 :
#   문장 1
#   문장 n
#   증가감 - 증가감이 없으면 반복을 종료할 수 없다(생략가능)

i = 1 # 초기값

while i <= 10: # 조건
    print(i, end=' ')
    i = i + 1


# 초기값이 없는 경우
# 증가감이 없는 경우
while 3 > 1:
    print("test", end = '')