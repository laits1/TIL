# len() :  문자열의 길이 반환
string = ("programming")
print(len(string))

# count : 문자열 내에 들어있는 특정 문자(열)의 개수 반환
# 변수(문자열).count("특정 문자(열)")

print(string.count("m"))
print("Python Programming".count("P"))

# find() : 문자열 내에서 특정 문자열이 존재하는지 여부와
# 문자열의 시작 위치를 반환
# 특정 문장려이 존재하면 시작 위치값 반환 / 존재하지 않으면 -1 반환
# 필터링하거나 문자열 검사, 추출할때 주로 사용

crawling = "Data crawling is fun"
print(crawling.find("fun"))             # 17
print(crawling[crawling.find("fun"):])  # fun
print(crawling.find("parsing"))         # 없으면 -1 반환
print(crawling.find("a"))               # 첫번째 문자 위치만 반환

# index() : 문자열 내에서 특정 문자열의 시작 위치를 반환
print(" ")

print(crawling.index("fun"))             # 17
print(crawling[crawling.index("fun"):])  # fun
# print(crawling.index("parsing"))         # 없으면 -1 반환
print(crawling.index("a"))               # 첫번째 문자 위치만 반환

# split() : 구분자를 기준으로 문자열을 나눔
# 나눈 결과를 리스트로 반환
# 구분자 : 기본 공백
# 구분자 지정 : "-", ":", "," , ....

string = "Python Programming"
string_split = string.split()
print(string_split) #['Python', 'Programming]

names = "홍길동, 이몽룡, 성춘향, 변학도" 
names_split = names.split(", ") # 구분자 : , 사용
print(names_split)

colors = "red:blue:yellow:green" # 문자열
colors_split = colors.split(":")
print(colors_split)


# 문자열과 리스트의 차이
for c in colors_split: # 리스트 출력
    print(c)


for c in colors: # 문자열 출력
    print(c)

# range() 에 list를 사용
for i in range(0, len(colors_split)) :
    print(colors_split[i])

# replace(): 전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변경
# 전체문자열.replace(찾는 문자열, 변경할 문자열)
# 찾는 문자열이 존재하면 변경될 문자열 반환
# 찾는 문자열이 없으면 원래 문자열을 그대로 반환

course = "Java Programming"
# Java -> Python 으로 변경
print(course.replace("Java","Python"))
# Web -> Python 으로 변경
print(course.replace("Web","Python"))

# join() : 각 문자 사이에 특정 문자(열) 삽입
a = "aa"
b = "bbb"
print(a.join(b))

# b-b-b 로 구성하고 싶으면
print('-'.join(b))

c_str = "대한민국" # 대*한*민*국
print("*".join(c_str))

# 리스트에서 join() 사용
sep = '-'
names = ["홍길동","이몽룡","성춘향"]
print(sep.join(names))

# upper(): 대문자로 / lower(): 소문자로 / 
# capitalize() : 문장의 첫 번째 문자를 대문자로
# title() : 단어의 첫 글자만 대문자로

print("-------------------------------------------")
string = "this is MY DOG."
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())


# 공백 제거
# strip() : 양쪽 공백 제거 
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거
s1 = "   hello   "
print("test",s1.strip(),"test")
print(s1.lstrip(),"test")
print("test",s1.rstrip())

# isalpha() : 문자 여부 결과 반환
# isdigit() : 숫자 여부 결과 반환
# isspace() : 하나의 문자에 대해 공백 여부 결과 반환
# isalnum() : 문자 또는 숫자 여부 결과 반환

phone = input("전화 번호 입력(숫자만) : ")

if phone.isdigit():
    pass
else :
    print("숫자만 입력하세요")

name = input("이름 입력 : ")
if not (name.isalpha()):
    print("문자만 입력하세요.")
else :
    print(f"이름은 {name}")

ID = input("ID 입력 : ")
# 문자 또는 숫자가 아닌 경우 : 
if not (ID.isalnum()):  # 문자 or 숫자 or 문자+숫자
    print("문자와 숫자만 사용할 수 있습니다.")

# 스페이스 여부 확인
print(" ".isspace()) # 스페이스 한 개 인 경우   True
print(" c".isspace()) # 다른 문자와 혼합        False
print("  ".isspace()) # 스페이스 두 개 인 경우  True

