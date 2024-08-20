#Fn = Fn-1 + Fn-2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,

n = int(input())

def fib(n):
    if n > 2:
        return fib(n-1) + fib(n-2)
    return 0 if n==0 else 1
print(fib(n))

def dpFib(n):
    fibList = [1,1]
    if n==0: return 0
    if n < 3: return 1
    for i in range(2,n):
        fibList.append(fibList[i-1]+fibList[i-2])
    return fibList[n-1]
print(dpFib(n))