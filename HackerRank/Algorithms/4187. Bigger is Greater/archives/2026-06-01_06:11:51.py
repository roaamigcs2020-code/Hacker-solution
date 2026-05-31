import math
import os
import random
import re
import sys
def biggerIsGreater(word):
    w=list(word)
    i=len(w)-2
    while i>=0 and w[i]>=w[i+1]:
        i-=1
    if i== -1:
        return "no answer"
    j=len(w)-1
    while w[j]<= w[i]:
        j-=1
    w[i],w[j]=w[j],w[i]            
    w[i+1:]=sorted(w[i+1:])
    return "".join(w)
import sys
lines=sys.stdin.read().splitlines()
n=int(lines[0])
for word in lines[1:n+1]:
    print(biggerIsGreater(word.strip()))

