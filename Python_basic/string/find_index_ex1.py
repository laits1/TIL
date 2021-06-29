email = input("이메일 입력 : ")
 

if email.find("@") == -1 \
    or email.find(".") == -1 \
    or email.find("@") > email.find(".") \
    or email.find(".") - email.find("@") == 1 \
    or email.find("@") == 0 \
    or email.find(".") == (len(email) - 1) \
    or email.count("@") >= 2 \
    or email.count(".") >= 2 :                           
    print("이메일 형식이 아닙니다.")
    print(f"입력한 이메일 : {email}")
else :                                              # 올바른 경우
    print(f"입력한 이메일 : {email}")
