print("===any()===")
#any(iterable) : 하나라도 참이면 True, 모두 거짓이면 False
# 전부 0이면 False, 아니면 True

print(any([0,0,0]))
print(any([0,1,0]))
print(any([0,"",[]]))   #, 빈문자열, 빈리스트 - False


print("===chr()===")
#chi(i) : 아스키코드 값에 해당하는 문자 반환
print(chr(65))  # A
print(chr(97))  # a
print(chr(13))  # enter

for i in range(65,97):
    print(chr(i))

print("===ord()===")
# ord(c) : chr 과 반대로 문자에 해당되는 아스키코드  값을 반환
print(ord("a"))
print(ord("0")) # 48
print(ord('\n')) # 10

print("===divmod()===")
# divmod(a,b) : a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(7,3))

print("== enumerate() ==")
# enumerate(iterable, start = 0)
# 시퀀스 형태의 값을 넘겨주면 index 값을 포함하는 enumerate 객체로 반환 해 주는 함수
# (리스트, 튜플, 문자열, range) -> 인덱스값, 실제값

# ['a','b','c'] => 0'a' 1'b' 2'c'

# enumerate 객체 반환 : <enumerate object at 0x000001E8BD72A680>
print(enumerate(["kim","Lee","Park"]))


for i, name in enumerate(["kim","Lee","Park"]):
    print(i,name)

# index 와 값을 나타내는 변수 명은 임의 사용 가능

for k, name in enumerate(["kim","Lee","Park"]):
    print(k,name)

# for 문처럼 반복되는 구간에서
# 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때

print("===eval===")
print(eval('1+2')) # 수식을 표현한 문장려을 실제 식으로 변환 후 연산결과를 반환

print("===filter() ===")
# filter(function, iterable) : 반복 가능한 자료형 요소돌이
# function에 입력되었을 때 반환값이 참인 것만 묶어서(걸러내서) 반환

# 양수만 반환하는 함수
def positive(x):
    return x > 0   # 함수 반환 결과가 True/False

print(filter(positive,[0,-1,5,-7,10])) # 필터 객체 반환
print(list(filter(positive,[0,-1,5,-7,10]))) # 리스트로 형변환

print("=== help()===")
# 내장 도움말 시스템 호출
help(print)

print("=== hex() ===")
# hex(): 정수를 "0x" 접수다가 붙은 소문자 16진수 문자열로 반환
print(hex(7))
print(hex(10))
print(hex(1024))

print("=== map ===")
# map(function이름, iterable) : iterable 각 요소가 함수 function에 의해 수행된 결과 반환

def increase(x):
    return x+1
print(map(increase,[1,2,3,4,5]))       # map 객체 반환
print(list(map(increase,[1,2,3,4,5])))


print("=== open() ===")
# 외ㅑ부 파일을 사용하기 위해 접근 경로르를 생성하는 함수 
file_write = open('my_file.txt','w')\

print("=== rount() ===")
# 실수를 반올림 하여 반환
# rount(number[실수, 몇째짜리까지 숫자나올건지])

print(round(3.141592,3)) # 3.142


print("=== zip() ===")
# zip(iterable, iterable1, ...) : 각 iterable 에서 동일한 인덱스의 요소를 추출하여 튜플 형태로 묶어서 반환

print(zip([1,2,3],[4,5,6]))
print(list(zip([1,2,3],[4,5,6])))   # [(1,4),(2,5),(3,6)]
print(list(zip([1,2,3],[4,5])))     # [(1,4),(2,5)]

# zip 함수를 사용해서 튜플로부터 딕셔너리 생성하는 예제
keys = ('apple','pear','peach')
vals = (300, 250, 400)

result = dict(zip(keys,vals))

print(result)


print("===sum()===")
#sum(iterable) : iterable의 모든 요소의 합 반환
print(sum([1,2,3,4,5]))