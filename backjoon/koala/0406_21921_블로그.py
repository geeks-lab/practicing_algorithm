N, X = map(int, input().split())

visits = list(map(int, input().split()))
sum_visits = sum(visits[:X])
max_visits = 0
cnt = 0

if sum(visits) == 0:
    print('SAD')
else:
    for i in range(N-X):
        sum_visits -= visits[i]
        sum_visits += visits[i + X]
        if sum_visits > max_visits:
            cnt = 1
            max_visits = sum_visits
        elif sum_visits == max_visits:
            cnt += 1


    print(max_visits, cnt, sep='\n')
