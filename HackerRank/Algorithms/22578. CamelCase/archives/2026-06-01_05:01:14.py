import math
import os
import random
import re
import sys
def camelcase(n):
    num=1
    for i in range(len(n)):
        if n[i].isupper():
            num+=1
    print(num)
n=str(input())
camelcase(n)
