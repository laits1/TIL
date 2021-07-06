# try:
#     print(10/0)     # 에러발생하면 무조건
# except:             # 본 구문으로 포커스가 넘어옴
#     print("오류발생")


# # 에러 종류 명시
# try:
#     print(10/0)     # 에러발생하면 무조건
#    # print("나이 : " + 23 + "살")    # TypeError
# except ZeroDivisionError:         # ZeroDivisionError만 처리
#     print("0 나누기 오류발생")

# 숫자를 입력하지 않은경우
try :
    num = int(input("숫자를 입력하세요 : "))

except ValueError as e:
    print("숫자가 아닙니다.", e)