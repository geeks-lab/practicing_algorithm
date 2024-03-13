from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    count = 1 

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
    return count

total_count = 0 
max_size = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            total_count += 1
            max_size = max(max_size, bfs(i, j))

print(total_count)
print(max_size)