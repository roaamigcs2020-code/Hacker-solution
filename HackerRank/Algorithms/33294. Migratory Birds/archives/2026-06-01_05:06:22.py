import math
import os
import random
import re
import sys
# Complete the 'migratoryBirds' function below.#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
def migratoryBirds(arr):
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    max_c=max(count.values())
    result=0
    for key in sorted (count):
        if count [key]== max_c:
            return key 
n=(int,input())
arr=list(map(int,input().split()))
print(migratoryBirds(arr))
