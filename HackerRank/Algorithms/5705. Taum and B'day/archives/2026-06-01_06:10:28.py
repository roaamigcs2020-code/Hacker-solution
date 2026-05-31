import math
import os
import random
import re
import sys
def taumBday(b, w, bc, wc, z):
    total=b*min(bc,wc+z)+w*min(wc,bc+z)
    print(total)
n=int(input())
for i in range(n):
    b,w=map(int,input().split())
    bc,wc,z=map(int,input().split())
    taumBday(b,w,bc,wc,z)
