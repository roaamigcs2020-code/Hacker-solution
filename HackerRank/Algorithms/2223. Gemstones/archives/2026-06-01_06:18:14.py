import math
import os
import random
import re
import sys
def gemstones(arr):
    unique=set(arr[0])
    r=[]
    for i in unique:
        for t in arr:
            if i not in t :
                break
        else:
            r.append(i)
    print (len(r))
n=int(input())
arr=[]
for i in range (n):
    s=str(input())
    arr.append(s)
    
gemstones(arr)    
