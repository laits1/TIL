list = []
while True:
    list.append(input("상품 등록 (엔터키 누르면 종료) : "))
    if list[-1] == '':
        break
for i in list:
    print(f"{i}", end=" ")