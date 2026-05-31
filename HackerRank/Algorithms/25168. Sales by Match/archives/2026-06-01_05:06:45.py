import math
import os
import random
import re
def salesMatch(arr):
    sum=0
    for i in range (len(arr)-1):
        for j in range (1,len(arr)-i):
            if arr[i]==arr[j+i] :
                sum+=1
                arr.pop(j+i)
                
                break
            
    return sum
n=(int,input())
arr=list(map(int,input().split()))
print(salesMatch(arr))
