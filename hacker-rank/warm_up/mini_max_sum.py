#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
test_data = [1, 5, 3, 7, 9]
print(type(test_data))

def miniMaxSum(arr):

    min_list = []
    max_list = []
    temp = 0
    min_sum = 0
    max_sum = 0


    # sorting the list
    sorted_list = sorted(arr)

    # puting in each list(min,max)
    for i in range(len(sorted_list)-1):

        # min_list
        min_list.append(sorted_list[i])
        # max_list
        temp += 1
        max_list.append(sorted_list[temp])

    # adding
    for i in range(len(sorted_list)-1):
        min_sum += min_list[i]
        max_sum += max_list[i]
    
    return min_sum, max_sum
    


miniMaxSum(test_data)
