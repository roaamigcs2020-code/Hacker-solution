import math
import os
import random
import re
import sys
def utopianTree(n):
    for i in range (n):
        num=int(input())
        s_num=1
        for j in range(1,num+1):
            if j % 2==0:
                s_num+=1
            else:
                s_num*=2
        print (s_num)
n=int(input())
utopianTree(n)
