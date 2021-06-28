num = int(input("도형 입력(1: 사각형, 2: 삼각형, 3: 원) : "))

if num == 1:
    width = int(input("가로 입력 : "))
    length = int(input("세로 입력 : "))
    print("사각형의 면적 = %.2f" %(width * length))
elif num == 2:
    width = int(input("밑변 입력 : "))
    height = int(input("높이 입력 : "))
    print("삼각형의 면적 = %.2f" % (width * height / 2))
elif num == 3:
    PI = 3.141592
    r = int(input("반지름 입력 : "))
    print("원의 면적 = %.2f" %(PI*r**2))