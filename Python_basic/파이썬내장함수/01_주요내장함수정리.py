print("===any()===")
#any(iterable) : 하나라도 참이면 True, 모두 거짓이면 False
# 전부 0이면 False, 아니면 True

print(any([0,0,0]))
print(any([0,1,0]))
print(any([0,"",[]]))   #, 빈문자열, 빈리스트 - False


print("===chr()===")
#chi(i) : 아스키코드 값에 해당하는 문자 반환
print(chr(65))  # A
print(chr(97))  # a
print(chr(13))  # enter

for i in range(65,97):
    print(chr(i))

print("===ord()===")
# ord(c) : chr 과 반대로 문자에 해당되는 아스키코드  값을 반환
print(ord("a"))
print(ord("0")) # 48
print(ord('\n')) # 10

print("===divmod()===")
# divmod(a,b) : a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(7,3))