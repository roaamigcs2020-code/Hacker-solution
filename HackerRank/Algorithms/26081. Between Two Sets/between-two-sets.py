import math
import os
import random
import re
import sys
# Complete the 'getTotalX' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
def BetweenTwosets(arr1,arr2):
    count=0
    for x in range(max(arr1),min(arr2)+1):
        if all( x% a == 0 for a in arr1):
            if all( b % x==0 for b in arr2):
                count+=1
    return count
n , m =(int,input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(BetweenTwosets(arr1,arr2))
