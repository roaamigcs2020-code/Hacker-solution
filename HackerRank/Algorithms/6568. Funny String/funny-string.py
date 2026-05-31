import math
import os
import random
import re
import sys

def funnyString(s):
    r=s[::-1]
    for i in range (1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(r[i])- ord(r[i-1])):
            print("Not Funny")
            return
    print("Funny")
n=int(input())
for i in range(n):
    s=str(input())
    funnyString(s)
