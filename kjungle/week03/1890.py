
# 점프 # 경우의 수 구하기
n = int(input())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

# 오른쪽으로 숫자만큼 이동 [i][j+current]
# 아래로 숫자만큼 이동 [i+current][j]

dp = [[0]* n for _ in range(n)]
dp[0][0]=1


for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
        
        # 현재 위치
        current = g[i][j]
        
        # 아래 이동(현재 위치 + 이동 위치)
        if i+current < n:
            dp[i+current][j] += dp[i][j]
        
        # 오른 이동
        if j+current < n:
            dp[i][j+current] += dp[i][j]
                
'''
'''


'''
def dfs(cur, visited):

    # 0 만나면
    if cur == 0:
        return cnt

    move_num = 0
    # 현재 가야되는 수
    for i in range(n):
        for j in range(n):
            move_num = g[i][j]
            # 아래 벽 만나면 -> g(4,1)ok,g(5,1)no
            if g[cur[0]][j] + move_num < n+1: # 여기 못함~
                # 수만큼 아래로 이동
                cur = g[i+1][j]
            # 오른 벽 만나면
            if g[i][cur[1]] + move_num < n+1: # 여기 못함~
                # 수만큼 오른쪽으로 이동
                cur = g[i][j+1]
'''
            
    
