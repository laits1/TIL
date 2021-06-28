notebook = 1200000
camera = 400000
print("*****상품 정보*****")
print(f"1 노트북 : {notebook:,} 원")
print(f"2 카메라 : {camera:,} 원")
print("*****상품 정보*****")
num = int(input("상품 번호 입력 : "))

if num == 1 or num == 2:
    num2 = int(input("주문 수량 입력 : "))
    print("***** 주문 내용 *****")

else:
    print("잘못 입력하였습니다. 종료합니다.")

if num == 1:
   print("상품명 : 노트북")
   print(f"가격 : {notebook:,} 원")
   print(f"주문 수량 : {num2}")
   print(f"주문액 : {notebook * num2:,} 원")
   print(f"할인액 : {int(notebook * num2 * 0.1):,} 원")
   print(f"총 지불액 : {int(notebook * num2 * 0.9):,} 원")
elif num == 2:
    print("상품명 : 디지털 카메라")
    print(f"가격 : {camera:,} 원")
    print(f"주문 수량 : {num2}")
    print(f"주문액 : {camera * num2:,} 원")
    print(f"할인액 : {int(camera * num2 * 0.05):,} 원")
    print(f"총 지불액 : {int(camera * num2 * 0.95):,} 원")