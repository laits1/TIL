# in/ not in 연산자
# 문자열 in 변수명(문자열)
# 결과는 True/False

string = "Python Programming"

print("Python" in string)
print("programming" in string) # False # 대소문자 구별
print("python" in string)   # False

if ("python" in string):
    print("있음")
else :
    print("없음")

if("thon" in string) :
    print("있음")
else :
    print("없음")

print("Python" not in "Python programming")

# 아래와 같이 ID가 저장되어 있는 list가 있다.
ids = ["sun", "flower", "moon", "sky"]

# 사용자가 입력 id가 list에 있으면 로그인 성공을 출력하고 
# 없으면 로그인 실패를 출력

ID = input("ID 입력 : ")

if ID in ids:
    print("로그인 성공")
else :
    print("로그인 실패")