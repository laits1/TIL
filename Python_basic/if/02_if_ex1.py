s_id = "flower"
s_password = "1234"
id = input("아이디 입력 : ")
password = input("비밀번호 입력 : ")

if id == s_id and password == s_password:
    print("로그인 성공!")
else:
    print("로그인 실패!")
