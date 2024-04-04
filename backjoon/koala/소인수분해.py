num = int(input())
divisor = 2

while num != 1:
    if num % divisor != 0:
        divisor += 1
    else:
        num //= divisor
        print(divisor)
    
