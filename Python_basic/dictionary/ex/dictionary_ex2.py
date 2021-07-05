eng_dic = {}
while True:
    word = input("영어 단어 등록 (종료는 quit) : ")
    if word in eng_dic.keys():
        print(f"{word}는 이미 등록된 단어 입니다.")
        continue
    if word == "quit":
        print()
        break
    else :
        mean = input(f"{word}의 뜻입력 (종료는 quit) : ")
        eng_dic[word] = mean
    
while True:
    find_word = input("검색할 단어 입력 (종료는 quit) : ")
    if find_word == "quit":
        print("\n종료합니다.")
        break
    if find_word in eng_dic.keys():
        print(f"{find_word}의 뜻은 {eng_dic[find_word]}입니다.")
    else :
        print(f"{find_word}는 사전에 없는 단어 입니다.")