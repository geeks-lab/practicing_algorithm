# def hano(n: int, a: int, b: int, c: int):
#     if n==1 :
#         print(a, c)
#     hano(n-1, a, c, b) # a -> b
#     print(a, c) # a -> c
#     hano(n-1, b, a, c) # b -> c


def hanoi(num, start, end):
    
    if num == 1:
        print(start, end)
        return
    else:
        hanoi(num-1, start, 6-start-end) # a -> b
        print(start, end) # a -> c
        hanoi(num-1, 6-start-end, end) # b -> c

N = int(input())

print(2**N -1)

if N <= 20:    
    hanoi(N, 1, 3)
    

    
