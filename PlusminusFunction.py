#!/bin/python3
###Minmax plus
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i == 0:
            zero = zero+1
        elif i>0:
            pos = pos+1
        else: 
            neg = neg+1
    posRa= "{:.6f}".format(float(pos/len(arr)))
    negRa="{:.6f}".format(float(neg/len(arr)))
    zeroRa="{:.6f}".format(float(zero/len(arr)))
    print(posRa)
    print(negRa)
    print(zeroRa)
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)