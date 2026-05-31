import math
import os
import random
import re
import sys
def marsExploration(s):
    s=s.lower()
    num=0
    for i in range(len(s)):
        if i%3 == 0:
            if s[i] != "s":
                num+=1
        elif i % 3 ==1:
            if s[i] !="o":
                num+=1
        elif i%3 == 2:
            if s[i]!="s":
                num+=1
    print(num) 
s=str(input())
marsExploration(s)
