''' 문제 설명
(https://hongcoding.tistory.com/83)
현재 도시에서의 최소비용은 DP를 활용하고, 도시를 방문하는 것은 DFS를 활용.

visited라는 변수에 2진수로 거친 도시를 표시하였다.

0001(2) = 1 이라면 => 0번 도시만을 거침
0011(2) = 3 이라면 => 0, 1 번 도시를 거침
1111(2) = 15 이라면 => 0, 1, 2, 3 번 도시를 거침
'''
'''
최적해(최소값) = min(지금까지 최적해 ,(  남은 공간의 가치    +  현재 물건의 가치) )
                   [i-1],[j]  ,( [i-1][j-물건의무게] +    [i][j-1]    )
'''
n = int(input())

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]
print(dp) #n이2면 

# [[1000000000, 1000000000, 1000000000, 1000000000], 
# [1000000000, 1000000000, 1000000000, 1000000000]]

def dfs(x, visited):
    # print('graph in dfs: ',graph) [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]

    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면,  10000 이라면
        # print('(1 << 4)', (1 << n)) -> 16
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))