n = int(input())

print((2**n)-1)

def hanoi(n, origin, temp, dest):
    # 종료조건
    if n == 1:
        return print(origin, dest)
    hanoi(n-1, origin, dest, temp)
    print(origin, dest)
    hanoi(n-1, temp, origin, dest)
    
# A -> B (origin to temp)
# A -> C (Bottom to dest)
# B -> C (temp to dest)

hanoi(n, 1, 2, 3)
