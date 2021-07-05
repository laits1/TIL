def get_interest():
    deposit = int(input("예금액 입력 : "))
    int_rate = eval(input("이자율 입력(%) : "))
    return int(deposit * int_rate / 100)
print(f"이자액 : {get_interest():,}원")