# 문자열
# 문자의 나열 - 여러 문자로 이루어져 있기 때문에 한 문자당 하나의 메모리 공간을 차지한다.
# "abc" -> a 한칸 b 한칸 c 한칸의 공간을 차지하고 공간이 연속되어 있음

# 인덱싱과 슬라이싱이 가능

# 문자열 생성 - '', "", """"""

crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

# 전체 문자열 출력(반환)
print(crawling)
print(crawling[:])

# 특정 인덱스의 문자 출력 - 파이썬의 인덱싱은 0부터 시작함
print(crawling[0])  # 첫번째 문자 : D
print(crawling[-1]) # 마지막 문자 : n
print(crawling[2])  # 인덱스 2번, 세번째 문자 : t

print("")
# 슬라이싱 예제
print(crawling[0:4])    # 0번 인덱스부터 3번 인덱스 까지 : Data
print(crawling[5:16])   # : crawling is
print(crawling[17])     # : f
print(crawling[19])     # : n
print(crawling[-1:])    # : n
print(crawling[-1])     # 위의 코드와 같음 : n
print(crawling[:-1])    # : Data crawling is fu
print(crawling[16:16+4])    # :  fun


print(" ")

print(parsing)          #Data parsing is also fun
print(parsing[5:])      #parsing is also fun
print(parsing[:15])     #Data parsing is
print(parsing[:])       #Data parsing is also fun


string = "happy day!!!"

string_a = string[:5] # 가능
print(string_a)
string[:5] = "abc" # 문자열의 부분 수정은 불가능

print(string)
