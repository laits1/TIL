## 함수 선언부 (클래스 선언부)
def add_data(data):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = data

def insert_data(position, data):
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    
    katok[position] = data


## 전역 변수부
katok = []
select = -1 # 1추가, 2삽입, 3삭제, 4종료



## 메인 코드부

if __name__ == '__main__' : # 메인 함수(진입점)
    while(select != 4) :
        select = int(input('선택 ( 1추가, 2삽입, 3삭제, 4종료) : '))

        if (select == 1):   # 추가 관련 코드
            data = input("추가할 데이터 : ")
            add_data(data)
            print(katok)

        elif (select == 2): # 삽입 관련 코드
            position = input("삽입할 위치 : ")
            data = input("추가할 데이터 : ")
            insert_data(position, data)
            print(katok)

        elif (select == 3):
            pass # 삭제 관련 코드
        elif (select == 4):
            pass # 종료 관련 코드
        else :
            print("1~4중에 입력하세요.")
        