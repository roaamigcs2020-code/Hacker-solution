import os
import sys
def getMoneySpent(key, b, drives):
    count=[]
    sum=0
    for i in range(len(key)):
        for j in range(len(drives)):
            sum= key[i]+drives[j]
            if sum<=b:
               count.append(sum)
    if count:
        return max(count)
    else:
        return -1
b,n,m=map(int,input().split())    
key=list(map(int,input().split()))
drives=list(map(int,input().split()))
print(getMoneySpent(key,b,drives))
