'''
방향 없는 그래프에서 연결 요소의 개수를 구하라
6 5
1 2
2 5
5 1
3 4
4 6

   0  1  2  3  4  5  6
0 [0][0][0][0][0][0][0]
1 [0][0][1][0][0][1][0]
2 [0][1][0][0][0][1][0]
3 [0][0][0][0][1][0][0]
4 [0][0][0][1][0][0][1]
5 [0][1][1][0][0][0][0]
6 [0][0][0][0][1][0][0]

연결 개수 초기화

현재 3이라고 할 떄 
    1 찾아서 (연결되어있는거찾기)
    (4, 3) 제외하고 
    (4, 6)거 찾아서 연결 노드로 이동
    찾은 노드가 (3,)이라면 
        3, 4, 6은 서로 연결되어 있음을 의미
        연결 개수 += 1

bfs 로 하는 방법도 있지만 unio find로 하는 방법이 더 괜찮으니 담에 코드 보기
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

graph = [[i] for i in range(n+1)] # 여기 틀림
# print(graph) # 6 5 -> [[0], [1], [2], [3], [4], [5], [6]]

for _ in range(m): # 간선 입력
    x, y = map(int, input().split())
    graph[x].append(y) # 여기 틀림
    graph[y].append(x)
  
# [[0], [1, 2, 5], [2, 1, 5], [3, 4], [4, 3, 6], [5, 2, 1], [6, 4]]

visited = [False] * (n+1)
cnt = 0 # 연결개수

# dfs(탐색할 그래프, 시작노드, 방문여부리스트)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]: # 방문하지않은 노드라면
            dfs(graph, i, visited)

# 연결 되었는지
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(graph, i, visited)

print(cnt)






