# append()
# a = [1,2,3,4]
# a.append(5) # a = [1,2,3,4,5]
# print(a)

# a.append([6,7]) # a = [1,2,3,4,5,[6,7]]
# print(a)

# # a.append(8,9) # 원소를 2개 추가하면 에러

# # 빈리스트 생성하고 요소 나중에 추가
# values = []
# values.append(10)
# values.append(20)
# values.append(30) # values = [10,20,30]
# print(f"values = {values}")

# # 사용자에게 5개의 값을 입력받아서 리스트에 저장
# scores = []
# for i in range(5):
#     num = int(input("값을 입력하세요 : "))
#     scores.append(num)

# print(f"score는 {scores}입니다.")

# # 위 코드에서 입력 받은 값을 각 요소로 출력
# for i in range(len(scores)):
#     print(scores[i], end=" ")
# print()
# for score in scores:
#     print(score, end= " ")

## insert(인덱스 값, 값) : 리스트 특정 위치에 요소 삽입
#                          그 뒤의 값들은 한칸씩 뒤로 밀림.
nums = [1,2,3,4,5]
nums.insert(1,200)      # nums = [1,200,2,3,4,5]
print(nums)

nums.insert(-1,"홍길동")
print(nums)

# insert 함수를 이용해서 맨뒤에 삽입 / append()쓰기!
nums.insert(len(nums),99)
print(nums)

nums.insert(len(nums)-1,[10,20])
print(nums)











