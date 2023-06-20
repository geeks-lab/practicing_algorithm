#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    
    for i in range(len(arr[0])):
        left_diagonal = left_diagonal + arr[i][i]
        right_diagonal = right_diagonal + arr[i][len(arr[0])-i-1]

    answer = abs(left_diagonal - right_diagonal)

    return print(answer)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

  
