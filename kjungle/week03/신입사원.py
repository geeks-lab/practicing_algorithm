import sys

# 테스트 케이스의 개수를 읽어옵니다
T = int(sys.stdin.readline())

# 각 테스트 케이스를 처리하는 반복문을 시작합니다
for _ in range(T):
    # 이번 테스트 케이스에서의 참가자 수를 읽어옵니다
    n = int(sys.stdin.readline())
    
    # 참가자들의 순위 정보를 리스트로 읽어옵니다
    rank = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 참가자들을 점수(첫 번째 요소)를 기준으로 정렬합니다
    rank.sort(key=lambda x: x[0])

    # 더 나은 순위를 가진 참가자들의 수를 세는 변수를 초기화합니다
    cnt = 1

    # 이전 최고 순위자의 순위를 첫 번째 참가자의 순위로 초기화합니다
    maxRank = rank[0][1]

    # 정렬된 참가자 목록을 반복하면서 처리합니다
    for i in range(n):
        # 현재 참가자의 순위가 이전 최고 순위보다 낮은지 확인합니다
        if rank[i][1] < maxRank:
            # 그렇다면, 더 나은 순위를 가진 참가자 수를 증가시키고 최고 순위를 업데이트합니다
            cnt += 1
            maxRank = rank[i][1]

    # 더 나은 순위를 가진 참가자들의 수를 출력합니다
    print(cnt)

