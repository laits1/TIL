# 아래 리스트에 저장되어 있는 점수에 대하여 합격/불합격을 판별하는 프로그램을 작성
# 합격은 60점 이상으로 설정

# 출력양식
# 1번 90점 합격
# 2번 57점 불합격

scores = [90,57,88,45,78]
num = 0
for score in scores:
    num += 1
    if score >= 60:
        result = "합격"
    else:
        result = "불합격"

    print(f"{num}번 {score}점 {result}")