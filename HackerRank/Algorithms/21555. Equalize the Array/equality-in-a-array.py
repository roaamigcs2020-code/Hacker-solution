import math
import os
import random
import re
import sys
def equalizeArray(arr,n):
    min_len=0
    for j in range(n):
        g=0
        for i in range(n):
            if arr[i]==arr[j]:
                g+=1
        if min_len<g:
            min_len=g
    print(n-min_len)
n=int(input())
arr=list(map(int,input().split()))
equalizeArray(arr,n)
