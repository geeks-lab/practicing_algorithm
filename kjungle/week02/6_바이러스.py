'''
입력
첫쨰줄 - 컴터 수 = 노드 수
둘째줄 - 총 간선 수
셋째줄 - 간선들

1과 연결 되어있는 노드의 수 구하기

'''

import sys
from collections import deque #q.pop 대신 시간복잡도가 낮은 popleft()사용하기 위해


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)] # 초기화

for i in range(m): # 간선 입력
    a, b = map(int, input().split())
    graph[a].append(b) # 양방향
    graph[b].append(a)

visited = [False] * (n+1)
num_v_connected = 0

def bfs(graph, v):
    global num_v_connected
    q = deque([v]) # 큐 초기화
    visited[v] = True # 방문처리
    
    while q: # q안에 데이터가 없을 때 까지
        popped = q.popleft() # q맨앞 값 꺼내
        visited[popped] = True

        #print(v, end=' ') # 출력 -> 1 2 5 3 6 
        for i in graph[popped]:
            if visited[i] == False: # 방문한적 없다면
                visited[i] = True
                q.append(i) # q에 추가
                num_v_connected += 1    

    print(num_v_connected)


bfs(graph, 1)