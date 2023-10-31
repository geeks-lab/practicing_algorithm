
'''
(M X N) X (A X B)

* 이 두개의 행렬을 곱할 때 N과 A가 같아야 가능하다
* 곱셉의 결과 -> M X B 
* 연산의 수 -> M X N X A

'''

def multi(i,j):
    if i == j:
        return 0
    _min = -987123

    for k in range(i,j):
        _min = min(multi(i,k) +
                   multi(k+1,j)+
                   'Pi-1 Pk Pj')
        


dp = [[-INF] * (n + 1) for _ in range(m + 1)]
def multi(i,j):
    if i == j:
        return 0
    
    if dp[i][j] != -987123:
        return dp[i][j]

    _min = -987123

    for k in range(i,j):
        _min = min(multi(i,k) +
                   multi(k+1,j)+
                   'Pi-1 Pk Pj')
    
    dp[i][j] = _min
    return dp[i][j]