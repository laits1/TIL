# 정수
a = 0b10 # 0b 2진수
b = 300 # 10진수
c = 0o123 # 8진수
d = 0x12fc # 16진수


print(a,b,c,d)
print(d)

# 실수

f = 3.14
f1 = -1234.45
f2 = 1.234567e5 # e5 소수점 다섯자리 오른쪽
f3 = 123456.7e-5
print(f,f1,f2,f3)

# 문자열

char1 = 'A'
char2 = 'B'

print(char1,char2)

str1 = '홍길동'
str2 = 'Python'
str3 = """여러줄로
나눠도됨"""
print(str1,str2)
print(str3)

#논리값/ 특수 리터럴
t=True
f=False

print(t,f)

val = None
val1= ""

print(type(val),type(val1))
print(val,val1)

print("긴 문장을 입력할 때 중간에서 엔터키를 치면"
      "다음행으로 가고 자동으로 따옴표 처리되면서"
      "한 줄로 인식되고 한줄로 출력")
# 세미콜론(;) 을 사용해서 한 행에 입력 가능
print("한줄에"); print("두개의 명령어")