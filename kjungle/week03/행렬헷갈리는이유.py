# 주의사항 row와 col을 위에서 바꿔서 받지 않으면 3x4아니라 4x3 나오니까 입력 자체를 거꾸로 받자.
col, row = map(int,input().split())

# 3x4 테이블 만들고싶다면, 근데 0번 인덱스 안쓸거라면?
dp = [[0] * (col+1) for _ in range(row+1)]


graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))
print(graph)


'''
[[0, 10, 15, 20], 
[5, 0, 9, 10], 
[6, 13, 0, 12], 
[8, 8, 9, 0]]
'''


# 0번 버리고 아래 인덱스를 이용해서 원하는 곳으로 접근해보기

# row 3 by col 4 짜리 만들건데
# 거꾸로 받아서 col 값 3, row 값 4 들어있음
#for i in range(1, row+1):  # row(4)+1 = 5니까 i는 1부터 4까지 4번 반복
    #for j in range(1,col+1): # col(3)+1 = 4니까 j는 1부터 3까지 3번 반복
        # 내가 현재 dp[4][3] 일때  내 왼쪽 애 출력해보기
        


# print(graph)