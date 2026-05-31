import math
import os
import random
import re
import sys
def BirthCake(arr):
    i=0
    n=max(arr)
    for g in range (len(arr)):
        if  arr[g] >= n:
            i+=1
    return i
            
        
        
n=int(input())
arr=list(map(int,input().split()))
print(BirthCake(arr))
