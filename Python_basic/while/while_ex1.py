price = 2000
balance = 10000
num = 0
while True:
    num += 1
    print(f"노래를 {num}곡 불렀습니다.")
    balance -= price
    if balance == 0:
        print("잔액이 없습니다. 종료합니다.")
        break
    print(f"현재 {balance}원 남았습니다")
