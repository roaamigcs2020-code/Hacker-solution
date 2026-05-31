import math
import os
import random
import re
import sys
def hackerrankInString(s):
    sen="hackerrank"
    s=s.lower()
    i=0
    for c in s:
        if c == sen[i]:
            i+=1
            if i == len(sen):
                break
    if i == len(sen) :
        print("YES")
    else:
        print("NO")
n=int(input())
for i in range (n):
    s=str(input())
    hackerrankInString(s)
