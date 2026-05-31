import math
import os
import random
import re
import sys
def jumpingOnClouds(n,arr):
    j=0
    i=0
    while i<n-1:
        if i+2<n and arr[i+2]==0:
            i+=2
        else:
            i+=1
        j+=1
    print(j)
n=int(input())
arr=list(map(int,input().split()))
jumpingOnClouds(n,arr)
