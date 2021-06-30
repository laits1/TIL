## sort() : 리스트 정렬, 원본 리스트 변경

scores = [90,78,81,64,89]
scores.sort() # 기본 : 오름차순 정렬
print(scores) # [64,78,81,89,90]

scores = [90,78,81,64,89]
scores.sort(reverse=True) # 내림차순 정렬
print(scores) # [90,89,81,78,64]

scores = [90,78,81,64,89]
scores.reverse() # 원소의 위치를 역순으로
print(scores) # [89,64,81,78,90]

## 문자의 정렬 - 대문자 < 소문자 , a~z, A~Z
char = ['B','A','d','C']
char.sort()
print(char) #['A','C','b','d']

# 대소문자 구별없이 정렬
# key = str.lower
char = ['b','A','d','C']
char.sort(key=str.lower)
print(char)


# 대소문자 구별 없이 내림차순 정렬
char = ['b','A','d','C']
char.sort(key=str.lower, reverse=True)
print(char) #['d','C','b','A']

# 문자열은 첫 문자로 정렬됨
ids = ['SKY', 'Blue','red','eBook','GREEN']
ids.sort() # 오름차순 정렬 - 첫 문자로 정렬
print(ids)

# 대소문자 구별 없이 정렬
ids = ['SKY', 'Blue','red','eBook','GREEN']
ids.sort(key=str.lower) # 오름차순 정렬 - 첫 문자로 정렬
print(ids)


## sorted() : 원본 유지하면서 정렬된 새로운 리스트를 반환
a = [3,5,2,1,4]
b = sorted(a)

print(a)
print(b)


## index()
# 리스트 안에서 원소의 위치 값 반환
# 리스트.index(값)
a = [1,2,3,4,5,5]
print(a.index(3)) #2
print(a.index(5)) #4
# print(a.index(10)) #에러

# min() : 리스트 내에서 최소값 원소 반환
# max() : 리스트 내에서 최대값 원소 반환
print("=================================")
n = [100,7,-2,99,30]
char = ['c','a','D','A','b']
n_char = [1,300,'a','D',-2]

print(min(n))
print(max(n))

print(min(char))
print(max(char))

# 복합 자료형 인 경우, max, min 함수 사용 불가
#print(min(n_char)) # 에러
#print(max(n_char)) # 에러

##in / not in (포함여부 판단후 True/False로 반환)
num = [1,2,3,4,5]
result = 2 in num       # num에 2가 있니?
print(result)           # True

result = 2 not in num   # num에 2가 없니?
print(result)           # False


## 리스트 일치 검사
# 비교 연산자를 사용해서 2개의 리스트 비교 (==, !=, >=, <=, <, >)
# 첫번째 요소부터 비교 시작
# 첫번째 요소의 비교에서 결과가 False면
# 더이상 비교하지 않고 첫번째 요소가 동일하면 두번째 요소 비교.
# 리스트 안의 모든 요소 비교 결과가 True 면 : True 반환

list1 = [5,2,3]
list2 = [1,2,3]
print("")
print(list1>=list2)

