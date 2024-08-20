# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.


def factorial_fuc(n):
    if(n>1):
        return n * factorial_fuc(n-1)
    else:
        return 1


n = int(input())
print(factorial_fuc(n))

'''
5*factorial_fuc(4) 5*24 -> factorial_fuc(5) = 120
4*factorial_fuc(3) 4*6 -> factorial_fuc(4) = 24
3*factorial_fuc(2) 3*2 -> factorial_fuc(3) = 6
2*factorial_fuc(1) 2*1 -> factorial_fuc(2) = 2
1
'''


