c_var = 100
print(c_var)
del c_var # 변수를 삭제하는 명령어

# 코드 블럭 주석처리 ctrl + /


# 문자열 값 저장
# 문자열을 큰따옴표 사용 (작은따옴표도 사용가능)
# 여러 종류의 따옴표를 사용시에는 짝을 맞춰야 함

name = "홍길동"
std_name = '김철수'
pro_name = "이몽룡'교수'"

print(name)
print(std_name)
print(pro_name)

address = '서울시 강남구'
print(name, address)
print(name + "은 " +address + '에 삽니다.')

result = name + "은 " + address + "에 삽니다."

print(result)

## 문자와 숫자의 결합(연결)
age = 23

print(name + "은 " + str(age) + "살 입니다.")

## 사각형의 면적을 구해서 출력하는 프로그램
# 넓이 : 100
# 높이 : 200

width = 100
height = 200

area = width * height
print(area)