
import sys

str1 = sys.stdin.readline()
str2 = sys.stdin.readline()

m,n = len(str1), len(str2)
dp = [[-1] * (n + 1) for _ in range(m + 1)]