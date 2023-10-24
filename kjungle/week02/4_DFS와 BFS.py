
#https://kill-xxx.tistory.com/entry/Python-DFSBFS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1260-%EA%B7%B8%EB%A6%BC-%ED%92%80%EC%9D%B4
'''
입력: 첫줄 - N M V
        (정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V)
     다음줄 - M개의 줄에 간선이 연결하는 두 정점의 번호
출력: 첫줄 - DFS 수행 결과
    다음줄 - BFS 수행 결과
4 5 1
1 2
1 3
1 4
2 4
3 4
[첫번째 줄 입력]
input N(노드의 수) M(간선 수) V(시작지점)
        4         5         1

[두번째줄 ~ M+1 째줄 입력]
1   2
1   3
1   4
2   4
3   4

   0  1  2  3  4
0 [0][0][0][0][0]
1 [0][0][1][1][1]
2 [0][1][0][0][1]
3 [0][1][0][0][1]
4 [0][1][1][1][0]

''' 
import sys
from collections import deque #q.pop 대신 시간복잡도가 낮은 popleft()사용하기 위해
input = sys.stdin.readline


n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)] # 초기화

for i in range(m): # 간선 입력
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited1 = [False] * (n+1) # n+1 하는 이유: 정점이 1~4 까지라서 0번인덱스사용안하려고
visited2 = [False] * (n+1)

# dfs: 시작점 v부터 숫자가 작은 노드부터 방문 -> 1, 2, 4, 3
def dfs(v):
    visited1[v] = True # 방문 처리
    print(v, end=" ") # 방문 후 정점 출력
    for i in range(1, n+1): 
        if not visited1[i] and graph[v][i] == 1: # 방문 기록이 없고 인덱스에 값이 있다면(연결되있다면)
            dfs(i) #호출될 때마다 visted는 1이되고  재귀되어 v에 i가 들어간다.최종적으로 모두 방문하게 되면 visted = [0,1,1,1,1]

# bfs: 방문한 노드 큐에 삽입, 
#       큐에 있는 거 팝 한 후 인접노드를 큐에 삽입(인접노드 방문안했을 경우만)  -> 1, 2, 3, 4
def bfs(v):
    q = deque([v]) # 큐 초기화
    visited2[v] = True # 방문처리
    while q: # q안에 데이터가 없을 때 까지
        v = q.popleft() # q맨앞 값 꺼내
        print(v, end=' ') # 출력
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i] == 1: # 방문기록 없고 연결되있다면
                q.append(i) # q에 추가
                visited2[i] = True

dfs(v)
print()
bfs(v)
    