import math
import os
import random
import re
import sys
def repeatedString(s,n):
    a=0
    for i in range (len(s)):
        if s[i]=="a":
            a+=1
    total =( n//len(s))*a +sum(1 for i in range (n%len(s))if s[i]=="a")  
    print(total)     
s=list(input())
n=int(input())
repeatedString(s,n)
