n = [1,2,3,3,4,5,4,3]

n.remove(4) # 4를 제거하고 원본반영됨
print(n) 

# n리스트에서 원소값이 3인 원소를 모두 제거하시오.
# 3의 개수를 확인해야함
count = n.count(3)
for i in range(count):
    n.remove(3)

print(n)

n1 = [1,1,2,1]
n1.remove(1)
n1.remove(1)
n1.remove(1)
print(n1)

## pop() : 리스트 마지막 요소 반환하고 삭제
x = ['a', 'b', 'c', 'd']
y = x.pop() # 'd'
print(y) # 반환된 마지막 요소 d
print(x) # d가 삭제된 나머지 요소만 확인 ['a','b','c']

# x에 남아있는 요소 3개를 pop


#