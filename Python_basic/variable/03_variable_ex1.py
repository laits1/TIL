name = "홍길동"
no = 2016001
year = 4
grade = 'A'
average = 93.5
level = 10
print("성명 : " + name)
print("학번 : " + str(no))
print("학년 : " + str(year))
print("학점 : " + grade)
print("평균 : " + str(average))

print("학점 : ", year)

print("나는 %s" %name)

# 문자 : %c
# 문자열 : %s
# 정수 : %d
# 실수 : %f

print("성명 : %s\n학번 : %s\n학년 : %d\n학점 : %c\n평균 : %.2f" %(name,no,year,grade,average))
print("등급 : %d%%" %level)