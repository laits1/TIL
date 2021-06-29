
# 2중 for문 사용해서
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
a = 1
for i in range(3):
    for j in range(4):
        print(f"{a} ", end=" ")
        a +=1
    print(" ")