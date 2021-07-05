members = []
for i in range(3):
    members.append(input("회원 입력 : "))

print("회원명단 : ", end="")
for member in members:
    print(member, end=" ")