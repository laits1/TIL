# 리스트 만들기
# 변수명 = [값1, 값2, ... 값n]
# 변수명 = [] - 빈 리스트 생성

#단일 자료형 list
ints = [1, 2, 3, 4, 5]
floats = [1.1, 2.2, 3.3, 4.4, 5.5]
names = ['홍길동', '이몽룡', '성춘향']

#복합 자료형 list
mix = [1, 5.0, '김철수']

# 리스트 안에 리스트를 포함할 수 있음
numbers = [100, 200, 300, [10,20,30]]

# 리스트 반환
# 리스트 명으로 접근
print(ints)
print(floats)
print(names)
print(numbers)

# 각 원소 접근

for name in names:
    print(f"{name}")
for number in numbers:
    print(f"{number}")

# 각 원소를 인덱스를 통해 접근
for i in range(0,len(numbers)):
    print(f"{numbers[i]}", end=" ")

# 리스트 각각의 값을 변수에 저장
nums = [1, 2, 3]
# 리스트 nums의 원소값 각각을 a,b,c 변수에 저장하시오
# a = nums[0]
# b = nums[1]
# c = nums[2]

a,b,c = nums # 리스트 각각의 값을 차례대로 앞의 변수에
print(nums)
print(a,b,c)


## 리스트 특징
nums1 = [10,20,30]
a1,b1,c1 = nums1

print(nums1)
print(a1,b1,c1)

