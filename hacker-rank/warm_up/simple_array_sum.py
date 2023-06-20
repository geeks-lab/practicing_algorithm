import math
import os
import random
import re
import sys

def simpleArraySum():
    n = int(input())
    nums = list(map(int,input().split()))
    sum = 0    
    for num in nums:
        sum += num
        
    return print(sum)

simpleArraySum()

