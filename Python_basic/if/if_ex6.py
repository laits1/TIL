notebook = 1200000
camera = 400000
print("*****상품 정보*****")
print(f"1 노트북 : {notebook:,} 원")
print(f"2 카메라 : {camera:,} 원")
print("*****상품 정보*****")
num = int(input("상품 번호 입력 : "))

if num != 1 and num != 2:
    print("잘못 입력하였습니다. 종료합니다.")

else:
    num2 = int(input("주문 수량 입력 : "))
    print("***** 주문 내용 *****")

    if num == 1:
        product = "노트북"
        price = notebook

    elif num == 2:
        product = "디지털카메라"
        price = camera
    
    # 주문액 계산
    amount = num2 * price
    # 할인액 계산
    if amount >= 1000000 :
        discount = int(amount * 0.1)
    elif amount > 500000 :
        discount = int(amount * 0.05)

    total = amount - discount

    print(f"상품명 : {product}")
    print(f"가격 : {price:,} 원")
    print(f"주문 수량 : {num2}")
    print(f"주문액 : {amount:,} 원")
    print(f"할인액 : {discount:,} 원")
    print(f"총 지불액 : {total:,} 원")