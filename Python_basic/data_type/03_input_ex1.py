kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
total = kor + eng + math
average = total / 3
print("총점 : %d" %(kor+eng+math))
print("평균 : %.2f" %average)