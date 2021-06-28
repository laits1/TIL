# 정수 10개를 사용자로부터 입력받아서 양,음,0의 개수 출력하는 프로그램

# 입력 양식
# 숫자 1 입력 : -1
# 숫자 2 입력 : 9
# ...
# 숫자 10 입력 : 5

#

yang = um = zero = 0
for i in range(1,11):
    n = int(input(f"숫자 {i} 입력 : "))
    if n > 0:
        yang += 1
    elif n < 0:
        um += 1
    else:
        zero += 1
print(f"양수 {yang}개, 음수{um}개, 0 - {zero}개")