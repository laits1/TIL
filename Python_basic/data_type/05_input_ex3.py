deposit = eval(input("예금액 입력 : "))
rate = eval(input("이자율 입력(%) : "))
deposit_rate = deposit * rate * 1/100
print("-------------------")
print("예금액 : %d 원" %deposit)
print("이자율 : %.1f %%" %rate)
print("예금이자 : %d 원" %deposit_rate)
print("잔액 : %d 원" %(deposit + deposit_rate))
print("-------------------")

print("예금액 : " + format(deposit,',') + "원")
print("이자율 : %.1f %%" %rate)
print("예금이자 : " + format(int(deposit_rate), ',') + "원")
print("잔액 : " + format(int(deposit + deposit_rate), ',') + "원")

# 쉼표를 붙이면 숫자가 아닌 문자열이 되므로 %s
print("예금액 : %s 원" % format(deposit, ','))

# 또는 포맷 코드 사용하지 않고 출력
print("예금액 : ", format(deposit, ','), " 원")