import math
import os
import random
import re
import sys
def drawingBook(n,p):
    front=(p//2)
    back=(n//2- p//2)
    return min(front,back)    
n=int(input())
p=int(input())
print(drawingBook(n,p))
