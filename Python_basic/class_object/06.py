# method type
# instance method - 객체로 호출(일반 method)
# 메쏘드는 객체 레벨로 호출 되기 때문에, 해당 메쏘드를 호출한 객체에만 영향을 미침
# class method(static method) – @staticmethod 사용
# 클래스 메쏘드의 경우, 클래스 레벨로 호출되기 때문에, 클래스 멤버 변수만 변경 가능
# class Math:    @staticmethod    def add(a, b):        return a + b    @staticmethod    def multiply(a, b):        return a * bMath.add(10, 20)Math.multiply(10, 20)
