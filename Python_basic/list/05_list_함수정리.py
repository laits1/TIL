a = [1,2,3,3,5]

## len()
# 리스트의 길이 반환
print(f"len() 함수 테스트 : {len(a)}") # 5 - 리스트 a의 원소 개수

## count() - 리스트 객체 메서드
# 리스트 내의 특정 요소의 개수 세기
# 리스트.count(요소)

print(f"count()함수 테스트 : {a.count(3)}")

print("-----------------------")

## append() : 리스트의 끝에 새로운 요소 추가
# 리스트.append(새로추가할요소)

## insert() : 리스트의 특정위치에 요소 삽입
# 리스트.insert(삽입위치, 새로추가할요소)
# 06_list_append_insert.py에 정리


## remove() : 리스트에서 값에 해당되는 요소 제거
# 리스트.remove(제거할 요소 값)
# 동일한 값이 여러개 있는 경우 첫 번째 값만 제거
# 동일한 값 모두 제거하려면 for 문 사용

## pop() : 값을 반환하고 삭제
# 리스트.pop()
# 리스트의 요소 반환 하고 삭제
# 리스트.pop(인덱스값)
# 인덱스 위치에 있는 요소 반환 삭제
# 07_list_remove_pop.py에 정리

## extend()
# 리스트의 확장
# 리스트.extend()
# extend는 리스트 원소가 추가되면 리스트가 확장됨 - 하나의 리스트
# append, insert는 추가된 원소가 리스트면 하위 리스트로 추가됨 - 리스트 안에 리스트
a = [1,2,3]
a.extend([4,5])
print(f"a리스트 : {a}")

b = [1,2,3]
b.append([4,5])
print(f"b리스트 : {b}")

## sort() / reverse() / sorted() : 원소의 정렬과 관계 되는 함수
# 08_list_sort.py에 정리

## index()








