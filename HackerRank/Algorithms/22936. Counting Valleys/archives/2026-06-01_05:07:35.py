import math
import os
import random
def countingValley(n):
    sum=m=v=0
    for i in arr:
        if i=="U":
            sum+=1
        elif i=="D":
            sum -=1
        if  sum<0 or sum==0:
            if sum <0 and m==0:
                m+=1
            elif sum==0 and m==1:
                m-=1
                v+=1
    return v
        
n=int,input()
arr=input()
print(countingValley(n))
