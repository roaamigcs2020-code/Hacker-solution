import math
import os
import random
import re
import sys
#
# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
arr=[]
n=int(input())
for _ in range(n):
    row=list(map(int,input().split()))
    arr.append(row)

r_sum=0
l_sum=0
for i in range (n):
    r_sum += arr[i][i]
    l_sum += arr[i][n-1-i]
print(abs(r_sum-l_sum)) 



