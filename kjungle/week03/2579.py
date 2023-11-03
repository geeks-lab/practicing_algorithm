
# 계단오르기



# 이전에 두연속된 계단을 밟았았다면 
    # 두 계단 오르기

# else:
    # 한계단을 그냥 오를 때

import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*301
data = []
for i in range(1, n+1):
    hi = int(input())
    data.append(hi)
dp[0] = data[0]
dp[1] = data[1]+data[0]
dp[2] = max(dp[0]+data[2], dp[1])
for i in range(3, n):
    # 연속된 3개를 모두 밟으면 안된다
    dp[i] = max(dp[i-2]+data[i], dp[i-3]+data[i-1]+data[i])
    print(dp[i], i)
print(dp[n-1])