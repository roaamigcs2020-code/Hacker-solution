import math
import os
import random
import re
import sys
def saveThePrisoner(n1):
    for i in range (n1):
        n,m,s=map(int,input().split())
        result=(s+m-1)%n
        if result==0:
            result=n
        print(result)
            
n1=int(input())
saveThePrisoner(n1)
