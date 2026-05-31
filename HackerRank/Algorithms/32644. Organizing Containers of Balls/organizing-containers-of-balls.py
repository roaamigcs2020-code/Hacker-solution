import math
import os
import random
import re
import sys
def organizingContainers(n):
    for i in range(n):
        n11=int(input())
        num=n11
        x=[]
        col_sum=[0]*num
        row_sum=[]
        for j in range (n11):
            c=list(map(int,input().split()))
            x.append(c)
            row_sum.append(sum(c))
            for k in range (num):
                col_sum[k]+=c[k]
        row_sum.sort()
        col_sum.sort()
        ok=True         
        for h in range(num):
            if row_sum[h]!=col_sum[h]:
                ok=False
        if ok==True:
            print("Possible")
        else:
            print("Impossible")      
n=int(input())
organizingContainers(n)
