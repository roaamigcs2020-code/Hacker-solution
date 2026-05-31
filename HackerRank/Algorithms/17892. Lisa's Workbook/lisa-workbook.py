import math
import os
import random
import re
import sys
def workbook(n, k, arr):
    num=0
    current_pg=1
    for h in range (n):
        total_question=arr[h]
        i=1
        while i<=total_question:
            end=min(i+k-1,total_question)
            for question in range(i,end+1):
                if question==current_pg:
                    num+=1
            current_pg+=1
            i+=k
    print(num)
n,k=map(int,input().split())
arr=list(map(int,input().split()))
workbook(n,k,arr)
