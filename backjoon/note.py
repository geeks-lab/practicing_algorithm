H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

print(H,M)