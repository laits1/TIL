A={1,2,3}
B={3,4,5,6}

# 합집합
# a|b
# a.union(b)
print(A|B)
print(A.union(B))

print("=========")
# 교집합
# a & b
# a.intersection(b)
print(A&B)
print(A.intersection(B))

print("===========")
# 차집합
# a - b
# a.difference(b)
print(A-B)
print(A.difference(B))