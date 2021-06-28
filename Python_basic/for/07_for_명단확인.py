for name in namelist:
    if search_name == name # 명단에서 이름을 찾은 경우 반복 중단
        find = True
        break # 반복 탈출 제어코드
    else:   # 명단에서 못찾은 경우 - 반복 끝가지 계속
        find =n False


#print(find)
if find: # if find ==True:
    print("명단에 있습니다")
else:
    print("명단에 없습니다.")
    