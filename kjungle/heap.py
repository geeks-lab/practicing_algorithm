# 힙을 구성하는 함수
def heapify(arr, n, i):
    largest = i  # 루트 노드를 가장 큰 값으로 설정
    left = 2 * i + 1  # 왼쪽 자식 노드
    right = 2 * i + 2  # 오른쪽 자식 노드

    # 왼쪽 자식 노드가 부모 노드보다 큰 경우
    if left < n and arr[i] < arr[left]:
        largest = left

    # 오른쪽 자식 노드가 부모 노드나 가장 큰 자식 노드보다 큰 경우
    if right < n and arr[largest] < arr[right]:
        largest = right

    # 가장 큰 노드를 부모 노드로 설정하고, 재귀적으로 힙을 구성
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# 힙 정렬 함수
def heap_sort(arr):
    n = len(arr)

    # 최대 힙을 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙에서 요소를 하나씩 추출하여 정렬된 리스트에 추가
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 루트 노드와 맨 마지막 요소를 교환
        heapify(arr, i, 0)  # 힙 구성

    return arr


# 힙 정렬 사용 예시
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("정렬된 배열:", sorted_arr)