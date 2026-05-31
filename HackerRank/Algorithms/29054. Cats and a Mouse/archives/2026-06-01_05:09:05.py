import math
import os
import random
import re
def catAndMouse(x, y, z):
    for i in arr:
        if abs(arr[0]-arr[2])<abs (arr[1]-arr[2]):
            return "Cat A" 
        elif abs(arr[0]-arr[2])>abs(arr[1]-arr[2]):
            return "Cat B"
        elif abs(arr[0]-arr[2])==abs(arr[1]-arr[2]):
            return "Mouse C"
q=int(input())
for i in range(q):
    arr=list(map(int,input().split()))
    x,y,z=arr[0],arr[1],arr[2]
    print(catAndMouse(x,y,z))
