import math
import os
import random
import re
import sys
def encryption(s):
    rows,cols=0,0
    n=len(s)
    if n!=0:
        import math
        rows=math.floor(n**0.5)
        cols=math.ceil(n**0.5)
        if rows * cols <n:
            rows+=1
    grid=[[""for j in range (cols)]for i in range (rows)]
    k=0
    for i in range (rows):
        for j in range(cols):
            if k<n:
                grid[i][j]=s[k]
                k+=1
    for c in range(cols):
        for r in range(rows):
            print (grid[r][c],end="")
        print(" ",end="")
    print()
s=input().replace(" ","")    
encryption(s)
