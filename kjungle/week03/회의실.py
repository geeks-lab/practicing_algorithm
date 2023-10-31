
n = int(input())

meetings = [tuple(map(int,input().split())) for _ in range(n)]

meetings.sort(key=lambda x:(x[1],x[0]))

cnt, endt = 0

for meeting in meetings:
    if endt <= meeting[0]:
        endt = meetings[1]
        cnt += 1

print(cnt)

'''
왜 가장 빨리 끝나는 것을 고르는가? -> 최적해인 이유 생각해보기(증명)
그렇다면 가장 늦게 시작하는 것부터 골라도 최적해일까? -> 맞다
'''