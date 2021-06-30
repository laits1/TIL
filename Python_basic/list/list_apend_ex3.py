list = []
cnt = total = average = 0
for i in range(5):
    list.append(int(input(f"학생{i+1} 점수 입력 : ")))
    total += list[i]
    average = total / (i+1)
    if list[i] >= 80:
        cnt += 1
print(f"총점 : {total}")
print(f"평균 : {average:.2f}")
print(f"80점 이상 학생 : {cnt}명")