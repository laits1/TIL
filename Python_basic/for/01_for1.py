#for 문 : 정해진 횟수만큼 반복할 때 주로 사용
# 문법
# for 반복요소를 저장할 변수 in 반복을 위한 리스트 또는 범위 :
#   반복문장1
#   반복문장2

# 리스트 ["홍길동", "이몽룡", "성춘향", "변학도"]의 요소를 모두 출력하시오.

for name in ["홍길동", "이몽룡", "성춘향", "변학도"]:
    print(name, end = ' ')

num = [1,2,3,4,5,6,7,8,9]
# 위 리스트의 요소들을 각각 출력하시오.
for n in num:
    print(n, end = ' ')

# ============================================================
# 반복 범위 설정 " range() 함수
# 특정 범위의 정수 생성
# range(start, stop, step)
# range(10)  start 생략, 10개의 정수, 0 ~ 9 까지의 정수 시작은 0
# range(1,10) step 생략
# range(1,10,2)
print()
for i in range(10):          # 0 ~ 9
    print(i, end = '')
print()
for i in range(1,10):        # 1 ~ 9
    print(i, end = '')
print()
for i in range(1,10,2):        # 1,3,5,7,9
    print(i, end = '')
print()
for i in range(10,1,-1):        # 10,9,8,7,6,5,4,3,2
    print(i, end = ' ')
print()
