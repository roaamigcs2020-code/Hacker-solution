import math
import os
import random
import re
import sys
def beautifulTriplets(d, arr):
    num=0
    for i in range(len(arr)):
        if (arr[i]+d) in arr and (arr[i]+2*d) in arr:
            num+=1
    print(num)
n,d=map(int,input().split())
arr=list(map(int,input().split()))
beautifulTriplets(d,arr)
