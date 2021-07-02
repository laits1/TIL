# 리스트를 함수에 인수로 전달할 때
def show_list(func_list): # list 변수의 주소가 전달되면서 같은 리스트를 참조
    func_list[0] = 10 # 원본 my_list도 변경됨
    print(func_list)
    print("1. func_list_id : ", id(func_list))

my_list=[1,2,3,4]
show_list(my_list)
print(my_list)
print("2. my_list id : ", id(my_list))