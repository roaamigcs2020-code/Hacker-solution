import math
import os
import random
import re
import sys
def alternatingCharacters(s,x):
    total=0
    for t in range (len(x)):
        s=x[t]
        num=0
        i=0
        while i < len(s)-1:
            if s[i]==s[i+1]:
                num+=1
            i+=1
        print(num)    
n=int(input())
x=[]
for i in range(n):
    s=str(input())
    x.append(s)
alternatingCharacters("",x)
    
