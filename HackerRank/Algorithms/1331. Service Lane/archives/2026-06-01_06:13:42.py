import math
import os
import random
import re
import sys
n,t=map(int,input().split())
arr=list(map(int,input().split()))
for _ in range (t):
    i,j=map(int,input().split())
    print(min(arr[i:j+1]))
