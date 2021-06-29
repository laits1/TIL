# 1부터 100 사이의 모든 3의 배수의 합을 while문을 이용해서 코드 작성

#누적 변수
sum = 0

# 초기값
num = 1
while num <=100:
    if(num % 3 == 0):
        sum += num
    num += 1

print(f"1~100까지 3의 배수의 합 : {sum}")