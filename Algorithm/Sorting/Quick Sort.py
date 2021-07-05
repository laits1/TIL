# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘
# 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# 가장 기본적인 퀵 정렬은 처 번째 데이터를 기준 데이터(Pivot)로 설정

# 피벗 값 '5', 왼쪽에서 5보다 큰 데이터 선택
# 오른쪽에서 5보다 작은 데이터 선택해서 서로 위치 교환
# 5 '7' 9 0 3 1 6 2 '4' 8
# 5 4 '9' 0 3 1 6 '2' 7 8
# 선택된 값의 위치가 엇갈린 경우 피벗과 작은 데이터 위치를 서로 변경
# 5 4 2 0 3 '1' '6' 9 7 8
# 1 4 2 0 3 5 6 9 7 8   # 피벗값'5' 왼쪽은 모두 5보다 작은 수, 오른쪽은 모두 5보다 큰 수
# 왼쪽 데이터 묶음 정렬
# 1 4 2 0 3 

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개 인 경우 종료
        return
    pivot = start       # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오르쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right+1, end)
quick_sort(array, 0, len(array) - 1)
print(array)
# 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도
# 최악의 경우 O(N^2)의 시간 복잡도
