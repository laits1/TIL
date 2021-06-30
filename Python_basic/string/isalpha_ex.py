str1 = input("문장을 입력하세요 : ")
alpha_cnt = digit_cnt = space_cnt = etc_cnt = 0

for i in range(0,len(str1)):
    if str1[i].isalpha():
        alpha_cnt += 1
    elif str1[i].isdigit():
        digit_cnt += 1
    elif str1[i].isspace():
        space_cnt += 1
    else :
        etc_cnt = len(str1) - alpha_cnt - digit_cnt - space_cnt
print(f"알파벳 : {alpha_cnt}개")
print(f"숫자 : {digit_cnt}개")
print(f"스페이스 : {space_cnt}개")
print(f"기타 : {etc_cnt}개")

