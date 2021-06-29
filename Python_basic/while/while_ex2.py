sum = 0
last_num = int(input("마지막 숫자를 입력하세요 : "))
tmp = last_num 
while tmp != 0:
    if (tmp % 2 != 0):
        sum += tmp
    tmp -= 1 
print(f"1부터 {last_num}까지의 홀수의 합은 {sum}입니다.")