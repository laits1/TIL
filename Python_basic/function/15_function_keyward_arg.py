# 학생 정보를 입력받아 학생 dict를 구성하여 반환하는 함수
def student_info(name,age,gender):
    student = {
        'name':name,
        'age':age,
        'gender':gender
    }
    return student

    # 함수 테스트
    # 함수 호출시 인수를 넘겨 dict가 제대로 구성되어 반환되는지 출력
print(student_info(name="kim",gender="여",age=23))  # 키워드 인수
print(student_info('lee',20,'남')) # 위치 인수
print(student_info('park',gender='남', age=25)) # 위치인수와 키워드인수 동시

### 주의 : 위치인수는 키워드 인수 앞에 있어야 한다.
# print(student_info(gender='남', age=22,'lee')) # 오류
