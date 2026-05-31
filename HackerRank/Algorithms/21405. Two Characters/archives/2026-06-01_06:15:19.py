import math
import os
import random
import re
import sys
def alternate(s):
    unique=list(set(s))
    max_len=0
    for i  in range (len(unique)):
        for j in range(i+1,len(unique)):
            temp=""
            for c in s:
                if c==unique[i] or c==unique[j]:
                    temp+=c
            valid=True
            for k in range(len(temp)-1):
                if temp[k]==temp[k+1]:
                    valid=False
                    break
            if valid and len(temp)>1:
                max_len=max(max_len,len(temp))
    print(max_len)
n=int(input())
s=input().strip()
alternate(s)
