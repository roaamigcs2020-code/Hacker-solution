import math
import os
import random
import re
import sys
# Complete the 'divisibleSumPairs' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
def divisibleSumPairs(n, k, ar):
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j]) % k==0:
                sum+=1
    return sum
n,k=map(int,input().split())
ar=list(map(int,input().split()))
print(divisibleSumPairs(n,k,ar))

        
