
# 최대 힙
'''
첫째줄 : 연산의 개수 (N)
둘째줄 : 자연수라면 x라는 값을 추가하는 연산. 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 제거하기.

'''

def heapify():
    # root, lc, rc
    
    # 자식끼리 비교 후 큰 자식이랑 부모랑 비교
    
    # 자식이 더 크면 swap
    
    # 바꿨으니까 다시 heapify



def heap_sort():
    # 1. heapify
    # 2. 맨 앞 인덱스랑 맨 뒤 인덱스 스왑
    # 3. heapify(2번에서 정렬 완료 된 거 빼고)


def solve():
    n, x = map(int, input())
    
    arr = []
    
    for i in range(n):
        arr.append(int(input))

    # x가 0보다 크면 값을 추가
    if x > 0:
        # d

    # 0이면 가장 큰 값 출력 후 값 제거
    if x == 0:
        print()
    