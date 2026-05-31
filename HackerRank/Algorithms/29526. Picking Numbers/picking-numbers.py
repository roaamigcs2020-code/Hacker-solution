import math
import os
import random
import re
import sys
def pickingNumber(arr):
    max_l=0
    arr.sort()
    for j in range (len(arr)):
        count=0
        for i in range (j+1,len(arr)):
            if abs(arr[j] - arr[i]) <=1:
                count+=1
            else:
                break
        count+=1
        if count> max_l:
            max_l =count
    return max_l
n=int,input()
arr=list(map(int,input().split()))
print(pickingNumber(arr))
