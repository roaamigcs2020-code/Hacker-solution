import math
import os
import random
import re
import sys
def beautifulBinaryString(n,b):
    i=0
    num=0
    while i <n-2:
        if b[i] == "0" and b[i+1]=="1" and b[i+2]=="0":
            num+=1
            i+=3
        else:
            i+=1
    print(num)   
n=int(input())
b=str(input())
beautifulBinaryString(n,b)
