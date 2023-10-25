
'''
# https://bmy1320.tistory.com/entry/%EB%B0%B1%EC%A4%80-Silver-1%EB%AC%B8%EC%A0%9C-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2178-%EB%AF%B8%EB%A1%9C-%ED%83%90%EC%83%89
4 6
101111
101010
101011
111011

'''

from collections import deque #q.pop 대신 시간복잡도가 낮은 popleft()사용하기 위해
# dx[0], dy[0] => 오른쪽 
# dx[1], dy[1] => 왼쪽 
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


n, m = map(int,input().split())

graph = []
 
for i in range(n): # 간선 입력
    graph.append(list(map(int, input())))

def bfs(x, y):
    q = deque() # 큐 초기화
    q.append((x, y))
    while q: # q안에 데이터가 없을 때 까지
        x, y = q.popleft() # q맨앞 값 꺼내
        for i in range(4): # 4 방향 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 칸이 미로의 벽에 닿는지
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # nx
                continue
            # 칸이 미로의 벽을 넘어가는지
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))

    # 마지막 값에서 카운트 값 뽑기
    return graph[n-1][m-1]

print(bfs(0,0)) 

        