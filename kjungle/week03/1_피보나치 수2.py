


n = int(input())

d = [0] * 100


# top down(recursive)
def top_down(n):
    # 종료조건 : 1 이나 2이면 무조건 1 반환
    if n == 1 or n == 2:
        return 1

    # 계산한 적이 있는 문제라면 그대로 반환
    if d[n] != 0:
        return d[n]

    # 계산한 적이 없는 문제라면 점화식으로 재귀
    if d[n] == 0:
        d[n] = top_down(n-1) + top_down(n-2)
        return d[n]

print('top_down result : ', top_down(n))


# bottom up
def bottom_up(n):
    # 1이랑 2는 미리 넣어놓기
    d[1] = 1
    d[2] = 1

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    
    print('bottom up result : ', d[n])

bottom_up(n)
    




