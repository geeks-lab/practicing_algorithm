#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase():
    stairs = int(input().strip())
    space = stairs-1
    for i in range(stairs):
        i += 1
        print(' ' * space + '#' * i)
        space -= 1


staircase()
