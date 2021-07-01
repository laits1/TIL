# 딕셔너리
# 키(key)와 값(value)의 한 쌍을 요소로 갖는 자료형
# 딕셔너리 = {키1:값1, 키2:값2, … }
# d = {1:’a’, 2:’b’, 3:’c’}
# 딕셔너리의 특징
# 순서가 없다. 따라서, 인덱스로 접근할 수 없다
# 중괄호 {} 사용
# key를 통해서만 접근
# key는 숫자, 문자 다 가능
# key:value 한 쌍을 item이라고 한다
# 쉼표(,)로 item 구분




d = {1:'a'}
print(d)
print(type(d))

# 두 번째 요소(item) 추가 (key-2, value-'b')
d[2] = 'b'  # 주의 2는 인덱스가 아님.
print(d)
 
d['test'] = 'ValueTest'
print(d)

print("=======================")
member = {'name':'홍길동','phone':'1234-1234','birth':'10/15'}
print(member)

#item 추가 : address :서울
member['address']='서울'
print(member)

#길면 여러줄로 입력해도 됨
naver = {'name':'naver', 'url':'www.naver.com',
         'userid':'nv', 'password':'1234'}
print(naver)

print("==========================")
#딕셔너리 주요 함수
# 딕셔너리.keys() : key만 추출해서 리스트로 반환
# [1, 2, 3]
# 딕셔너리.values() : value만 추출 리스트로 반환
# [‘a’, ‘b’, ‘c’]
# 딕셔너리.items() : 
# (key:value)의 튜플을 추출해서 리스트로 반환
# [(1:’a’), (2:’b’), (3:’3’)]


print(naver.keys())     # key 리스트형태로 변환
print(naver.values())   # value 리스트 형태로 변환
print(naver.items())    # (key,value) 리스트 변환

print(type(naver.keys()))     # key 리스트형태로 변환
print(type(naver.values()))   # value 리스트 형태로 변환
print(type(naver.items()))    # (key,value) 리스트 변환
print("==========================")

# 리스트로 변환 : list() 함수 사용
to_list= list(naver.keys())
print(to_list)
print(type(to_list))

# 튜플로 변환 : tuple() 함수 사용
to_tuple = tuple(naver.keys())
print(to_tuple)
print(type(to_tuple))

# 딕셔너리 특정 item value 참조 : key 이용
member = {'name':'홍길동','phone':'1234-1234','birth':'10/15'}
print(member['name'])

print("=============================")
# key 리스트의 각 요소 출력

for key in naver.keys():
    print(key)

print("=============================")

# value 값 출력
for value in naver.values():
    print(value)

# item 출력
for item in naver.items():
    print(item)
print("=============================")
# key로 value 찾기 : 딕셔너리 변수[key] 이용한 접근
# 딕셔너리변수.get(key) 이용한 접근

print(naver['userid'])
print(naver.get("password"))

# 존재하지 않는 경우 : link 키가 없는 경우
# print(naver['link']) # 에러
print(naver.get("link"))        # None
print(naver.get("link","없음")) # 없음

# if문에서 get()사용
insert_key = 'link'
if naver.get(insert_key) is None:
    print(insert_key + "에 대한 data가 없습니다.")

# 존재 여부만 확인 : in / not in
print('link' in naver)
print('link' not in naver)

#list/dic/tuple 관련 함수 확인 dir()사용
print("------------------------")
my_list = []
print(dir(my_list))

