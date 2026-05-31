import math
import os
import random
import re
import sys
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def compareTriplets(a, b):
    Alice=0
    Bob=0
    for i in range (3):
        if (1<= a[i] <=100 and 1 <= b[i]<=100):
           if a[i]> b[i]:
               Alice +=1
           elif a[i]<b[i]:
               Bob +=1
        else:
           print("your input must BW in 1 and 100")
    return(Alice,Bob) 
result=compareTriplets(a,b) 
print( *result)
    
    
    
