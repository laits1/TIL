list = []
total = average = 0
for i in range(5):
    list.append(int(input(f"학생{i+1} 점수 입력 : ")))
    total += list[i]
    average = total / (i+1)
print(f"총점 : {total}")
print(f"평균 : {average:.2f}")