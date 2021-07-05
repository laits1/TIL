import random
def gbb_game() :
    COM = random.randrange(1,4)
    YOU = int(input("YOU 입력 (1:가위, 2:바위, 3:보) : "))
    if COM == YOU:
        print("비겼습니다.")
    elif (COM == 1 and YOU == 3) or \
        (COM == 2 and YOU == 1) or \
            (COM == 3 and YOU == 2):
        print("컴퓨터가 이겼습니다.")
    else :
        print("당신이 이겼습니다.")
    print(f"COM : {COM}")
gbb_game()
