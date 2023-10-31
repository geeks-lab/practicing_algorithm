import sys

string_a = sys.stdin.readline().rstrip().upper()
string_b = sys.stdin.readline().rstrip().upper()

len_a = len(string_a)
len_b = len(string_b)

dp = [[0] * (len_b+1) for _ in range(len_a+1)]


def lcs(i,j):
    for i in range(1, len_a + 1):
        for j in range(1, len_b +1):
            if string_a[i-1] == string_b[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[i][j]     
print(lcs((len_a-1), (len_b-1)))

