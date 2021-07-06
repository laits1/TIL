#에러 (Error)
# 문법적 오류나 실행 시간에 잘못된 메모리 접근 오류, 논리 오류, 사용자의 잘못된 입력 오류 등
# 오류가 발생하면 프로그램 중단되고 에러 메시지 출력
# 발생되는 에러 예 :
# ZeroDivisionError : 0으로 나누었을 경우 
# FileNotFoundError : File을 못 찾았을 경우
# IndexError : 리스트 등에서 인덱스 잘못되었을 때


# 에외 처리 방법
# try ... except 문 사용

# 예외처리문 형식
# try:
#   (예외 발생 가능) 문장
# except 예외 유형:
#   예외처리 문장
# else :    # 생략 가능
#   예외 없을 때 수행문장
# finally:  # 생략 가능
#   예외 유무와 상관없이 항상 실행되는 문장


print("====== 에러 확인 =====")
#
# print(10/0)

# print("나이 : " + 23 + "살")    # TrypeError

# print(b)    # NameError

c = 100
# print("%d%"%c) # valueError

# if x > 10       # SyntaxError
#     print("홍길동")


a=[1,2,3,4]
# print(a[5]) # IndexError

# def add():
#     a = a+1

# add()         # UnBoundLocalError
#OSError : 파일 경로는 운영체제 권한이기 때문에 운영체제 에러
# 경로명에 \\ 두번사용하기
# f = open("C:\Users\SDG\Documents\TIL\file_t2.txt",'w')


