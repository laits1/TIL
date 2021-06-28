# 리스트 생성 문법
# 리스트 식별자 = [요소값 1, 요소값 2, .... , 요소값 n]
# 리스트는 크기는 가변적
# 다양한 종류의 데이터를 하나의 리스트에 저장 가능

scores = 100 # 변수
print(scores)
scores_list = [100, 200, 300, "사백"]
a = 2
print(scores_list[2:])  # 300, '사백'
print(scores_list[a:])  # 300, '사백'

print(scores_list[:2])  # 100, 200
print(scores_list[1:2]) # 200

## 아래 test_list 에서 '연습' 데이터만 출력하시오
test = ['연습']
print(test[0])

