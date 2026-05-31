import math
import os
import random
import re
import sys
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def sumPNZERO (n):
    p=0
    ne=0
    z=0
    for i in range (n):
        if arr[i]<0:
            p+=1
        elif arr[i]>0:
            ne+=1
        elif arr[i]==0:
            z+=1
    print (f"{ne/n:.6f}",f"{p/n:.6f}",f"{z/n:.6f}" , sep="\n")
n=int(input())
arr=list(map(int,input().split()))
sumPNZERO(n)
