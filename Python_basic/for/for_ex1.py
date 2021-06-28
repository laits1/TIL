num1 = int(input("숫자1 입력 : "))
num2 = int(input("숫자2 입력 : "))
result = 0
for i in range(num1,num2+1):
    result += i
print(f"{num1}부터 {num2}까지의 합 : {result}")