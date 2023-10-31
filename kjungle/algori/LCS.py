'''# Top-down(recursion) before applying DP
def lcs(i, j):
    # 기본 경우 (Base Case): 두 문자열 중 하나라도 길이가 0이면 최장 공통 부분 수열의 길이는 0입니다.
    if i == 0 or j == 0:
        return 0
    
    # 현재 문자를 최장 공통 부분 수열에 추가하고, 이전 문자열의 최장 공통 부분 수열 길이에 1을 더합니다.
    if str[i] == str[j]:
        return lcs(i-1 ,j-1) + 1
     
    # 현재 문자가 다르다면
    # 한 문자열의 끝에서 한 문자열의 문자를 제외한 경우와 다른 문자열의 문자를 제외한 경우 중 더 긴 최장 공통 부분 수열을 선택합니다.
    return max(lcs(i, j-1), lcs(i-1, j))
'''
import sys

str1 = sys.stdin.readline()
str2 = sys.stdin.readline()
m,n = len(str1), len(str2)
dp = [[-1] * (n + 1) for _ in range(m + 1)] # 여기틀림

# Top-down(recursion) after applying DP
def td_lcs_dp(i, j):
    if i == 0 or j == 0:
        return 0

    # 이미 계산한 결과가 메모에 저장되어 있다면 그 값을 반환
    if dp[i][j] != -1:
        return dp[i][j]
    
    # 현재 문자가 같다면
    if str1[i] == str2[j]:
        # 현재 문자를 최장 공통 부분 수열에 추가하고, 이전 문자열의 최장 공통 부분 수열 길이에 1을 더합니다.
        dp[i][j] = td_lcs_dp(i-1, j-1) + 1
        return dp[i][j]
    
    # 현재 문자가 다르다면
    # 한 문자열의 끝에서 한 문자열의 문자를 제외한 경우와 다른 문자열의 문자를 제외한 경우 중 더 긴 최장 공통 부분 수열을 선택합니다.
    dp[i][j] = max(td_lcs_dp(i, j-1), td_lcs_dp(i-1, j))

    return dp[i][j]

print(td_lcs_dp(m -1, n -1)) # 여기틀림






''' btm-up psuedo
# base
dp[0][0]=0
for (int i=1; i<str.length; i+1){
    for(int j=1;j<str.length; j+1){
        if(str1[i]==str2[j]){
            dp[i][j] = dp[i-1][j-1]+1;
            continue
        }
        dp[i][j]=max(dp[i][j-1],[i-1][j]);
    }
}
'''
# bottom-up after applying DP with two pointer
def btu_lcs_dp(str1, str2):
    m,n = len(str1), len(str2)
    
    # DP 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # DP 테이블 채우는 부분
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]: # 현재 문자가 같다면
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 현재 문자가 다르다면
                # 한 문자열의 끝에서 한 문자열의 문자를 제외한 경우와 다른 문자열의 문자를 제외한 경우 중 더 긴 최장 공통 부분 수열을 선택합니다.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # DP 테이블을 이용하여 최장 공통 부분 수열 길이 찾기

    lcs_length = dp[m][n]           # lcs_length는 최장수열의길이
    lcs = [''] * lcs_length         # LCS (최장 공통 부분 수열) 길이에 맞게 빈 문자열 리스트를 생성

    i, j = m, n                     # i와 j를 각각 문자열 str1과 str2의 길이로 초기화.
    index = lcs_length - 1

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]: # 현재 위치의 문자가 동일한 경우
            # 현재 LCS의 끝에 해당 문자를 추가하고, i와 j를 하나씩 감소.
            lcs[index] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1 # 아래 a 주석 참조
        elif dp[i - 1][j] > dp[i][j - 1]:# 현재 위치의 문자가 다른 경우
            i -= 1                      # dp 테이블의 위쪽 값이 더 크다면 i를 하나 감소시켜서 위로 이동
        else:
            j -= 1                      # dp 테이블의 왼쪽 값이 더 크다면 j를 하나 감소시켜서 왼쪽으로 이동
    
    # LCS 문자열을 문자열로 변환합니다.
    return "".join(lcs)

''' 예시 사용
str1 = "AGGTAB"
str2 = "GXTXAYB"
result = lcs(str1, str2)
print("최장 공통 부분 수열:", result)  # "GTAB" 출력
'''

''' [a]
while의 if문 마지막에 index -= 1 하는 이유 : 
    현재 LCS의 문자를 찾았을 때 이 문자를 'lcs' 리스트의 마지막 위치에 추가한 후 그 다음 위치로 이동하기 위함
    chatgpt says
    이 코드에서 lcs_length는 초기에 lcs 리스트의 마지막 인덱스를 나타내며, 
    매번 LCS 문자를 찾을 때마다 해당 위치에 문자를 추가한 후, 
    다음 문자를 저장할 위치로 이동하기 위해 lcs_length를 1 감소시킵니다. 
    이렇게 하면 lcs 리스트에 LCS 문자열이 역순으로 저장되는데, 
    이후에 "".join(lcs)를 사용하여 역순으로 저장된 LCS 문자열을 올바른 순서로 결합합니다.
    
'''