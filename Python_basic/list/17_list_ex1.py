print("사자성어 맞추기 게임을 시작합니다.")

list1 = ["미리 준비해두면 근심 걱정이 없다."]
list2 = ["유비무환"]

while True:
    word = input(f"{list1[0]}\n \
        이말의 사자성어는? : ")
    if word == list2[0]:
        print("맞습니다.. 게임을 종료합니다.")
        break
    else :
        print("\n틀렸습니다... 다시 도전 !\n")
        continue
