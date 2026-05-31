import math
import os
import random
import re
import sys
def pangrams(s):
    s=s.lower()
    num=0
    alp="qwertyuiopasdfghjklzxcvbnm"
    if (len(s))>=26:
        for i in alp:
            for p in range(len(s)):
                if i == s[p]:
                    num+=1
                    break
        if num== 26:
            print("pangram")
        else:
            print("not pangram")
    else:
        print("not pangram")        
s=str(input())
pangrams(s)
