n, snake_len = map(int, input().split())
fruits_heights = list(map(int, input().split()))

fruits_heights.sort()
for i in range(n):
    if snake_len >= fruits_heights[i]:
        snake_len += 1
    else:
        break

print(snake_len)


