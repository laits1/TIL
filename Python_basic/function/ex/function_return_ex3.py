def order():
    price = int(input("상품가격 입력 : "))
    quantity = int(input("주문수량 입력 : "))
    print("-------------")
    print(f"상품가격 : {price}원")
    print(f"주문수량 : {quantity}개")
    return price * quantity

print(f"주문액 : {order()}원")