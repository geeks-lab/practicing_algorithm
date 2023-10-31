
'''
https://velog.io/@yoonkeem/BOJ-11047%EB%B2%88-%EB%8F%99%EC%A0%84-0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
n = 동전 갯수
k = 총 금액
'''

n, k = map(int, input().split())

coins=list()

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

result = 0
for i in coins:
    if k == 0:
        break
    result += k // i
    k %= i

print(result)

'''
count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

'''


    