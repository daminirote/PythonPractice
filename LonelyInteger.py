import math
import os
import random
import re
import sys

def lonelyinteger(a):
    ans = 0
    for i in a:
        ans ^= i
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()