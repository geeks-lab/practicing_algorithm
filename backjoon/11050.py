# 자연수 (N\)과 정수 (K\)가 주어졌을 때 이항 계수 (\binom{N}{K}\)를 구하는 프로그램을 작성하시오.
# 이항계수 int result = factorial(n) / (factorial(k) * factorial(n - k));

import math

n, k = map(int,input().split())

print(int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k))))

# 함수사용 예시 print(math.comb(x,y))