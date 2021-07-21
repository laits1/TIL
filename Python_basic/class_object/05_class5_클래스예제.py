# 1. 숫자를 하나 증가하는 메서드
# 2. 숫자를 0으로 초기화 하는 메서드
# 3. 숫자를 저장하는 속성(멤버변수) - 생성자 함수
# 4. 현재 숫자값을 출력하는 메서드

class Counter : 
    def __init__(self) :
        self.num = 0

    def increment(self) :
        self.num += 1
    
    def reset(self) :
        self.num = 0

    def print_current_value(self) : 
        print("현재 저장되어 있는 값은 : ", self.num)

# 객체 생성
c1 = Counter()
c2 = Counter()

# 질문 : c1 인스턴스와 c2 인스턴스는 공통의 멤버변수 num을 사용한다(O/X)