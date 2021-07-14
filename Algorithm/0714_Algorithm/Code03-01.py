# 선형 리스트

katok = [] # 빈 배열

def add_data(friend):
    katok.append(None)  # 빈칸 추가
    kLen = len(katok)   # 배열의 길이
    katok[kLen-1] = friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)
