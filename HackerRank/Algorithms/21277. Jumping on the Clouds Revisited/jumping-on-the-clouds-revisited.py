import math
import os
import random
import re
import sys
def jumpingOnClouds(n,k,c):
    sum=100
    i=0
    while True:
        i=(i+k)%n
        if c[i]==1:
            sum-=3
        else:
            sum-=1
        if i==0:
            break
    print (sum)
n,k=map(int,input().split())
c=list(map(int,input().split()))
jumpingOnClouds(n,k,c)
