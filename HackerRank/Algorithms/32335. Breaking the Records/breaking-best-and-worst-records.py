import math
import os
import random
import re
import sys
# Complete the 'breakingRecords' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
def breakingRecords(game):
    c_min=0
    c_max=0
    min_g=game[0]
    max_g=game[0]
    for a in game[1:]:
        if a > max_g:
            c_max+=1
            max_g=a
        elif a< min_g :
            c_min +=1
            min_g=a
    return (c_min , c_max)
n=int(input())
game=list(map(int,input().split()))
result=breakingRecords(game)
print(result[1],result[0])
