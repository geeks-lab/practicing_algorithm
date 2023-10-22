
# 최대 힙
'''
첫째줄 : 연산의 개수 (N)
둘째줄 : 자연수라면 x라는 값을 추가하는 연산. 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 제거하기.

'''

import sys
import heapq

numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-1)*num) # min heap만 지원하기 때문에 num에 -붙여서 max화
    else: # 0이면 배열에서 가장 큰 값 출력하고 제거하기
        try:
            print((-1)*heapq.heappop(heap))
        except:
            print(0)

