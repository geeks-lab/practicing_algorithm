
import math
import os
import random
import re
import sys


test_data = [1, 5, 3, 7, 9]
print(type(test_data))

def miniMaxSum(arr):

    a = sorted(map(int,arr.split()))
    print(sum(a[:4]),sum(a[1:]))


    
    


miniMaxSum(test_data)



