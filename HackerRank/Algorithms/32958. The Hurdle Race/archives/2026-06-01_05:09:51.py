import math
import os
import random
import re
import sys
def theHurdleRace(k,n1):
    max_n1=max(n1)
    if k<max_n1:
        return max_n1-k
    else:
        return 0
          
n,k=map(int,input().split())
n1=list(map(int,input().split()))
print(theHurdleRace(k,n1))
