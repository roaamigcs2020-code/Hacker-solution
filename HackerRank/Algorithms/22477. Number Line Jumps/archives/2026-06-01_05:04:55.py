import math
import os
import random
import re
import sys
# Complete the 'kangaroo' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
x1=0
x2=0
v1=0
v2=0
def numberLineJump(x1,v1,x2,v2):
    if (v1>v2) and (x2-x1)%(v1-v2)==0:
        print ("YES")
    else:
        print("NO")
x1 ,v1,x2,v2=map(int,input().split())
numberLineJump(x1,v1,x2,v2)

