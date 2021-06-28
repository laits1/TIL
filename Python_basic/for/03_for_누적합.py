# 1붙너 10까지 출력하는 프로그램을 작성하시오
sum = 0
for i in range(1,11):
    print(i, end=' ')
    sum += i
print(f"누적 합 : {sum}")