def get_area():
    a = int(input("가로 길이 입력 : "))
    b = int(input("세로 길이 입력 : "))

    return a * b
print(f"사각형의 면적 : {get_area()}")