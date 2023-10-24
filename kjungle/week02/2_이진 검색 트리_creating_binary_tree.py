import sys
sys.setrecursionlimit(10**6)
n = 2**10001
number = []
tree = [0 for _ in range(n)]
def last(idx):
    if idx > n or not tree[idx]:
        return
    if idx * 2 < n and tree[idx * 2]:
        last(idx * 2)
    if idx * 2 + 1 < n and tree[idx * 2 + 1]:
        last(idx * 2 + 1)
    print(tree[idx])
# list = []
while True:
    try:
        number.append(int(sys.stdin.readline()))
    except:
        break
while len(number):
    tmp = number.pop(0)
    compN = 1
    while compN <= n:
        if not tree[compN]:
            tree[compN] = tmp
            break
        elif tmp < tree[compN]:
            compN *= 2
        else:  # tmp > tree[compN] :
            compN = compN * 2 + 1
        # print(f"compN {compN} tmp {tmp}")
# print(tree)
last(1)