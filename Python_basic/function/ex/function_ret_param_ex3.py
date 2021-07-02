def order():
    price = int(input("상품가격 입력 : "))
    quantity = int(input("주문수량 입력 : "))
    
    amount = price * quantity   # 주문액
    if amount >= 100000:
        discount = amount * 0.1 # 할인액
        total = amount - discount # 지불액
    elif amount >= 50000 and amount < 100000:
        discount = amount * 0.05 # 할인액
        total = amount - discount # 지불액
    elif amount < 50000:
        discount = 0
        total = amount - discount

    return int(amount), int(discount), int(total)
    
amount, discount, total = order()
print("-------------")
print(f"주문액 : {amount}원")
print(f"할인액 : {discount}개")   
print(f"지불액 : {total}원")