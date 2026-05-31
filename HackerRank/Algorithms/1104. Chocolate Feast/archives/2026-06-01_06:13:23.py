import math
import os
import random
def chocolateFeast(n, c, m):
    save,new_chocolate,Warning,num,count=0,0,0,0,0
    new_chocolate=n//c
    num+=new_chocolate
    save=new_chocolate
    Warning=0
    while save+Warning>=m:
        new_chocolate=(save+Warning)//m
        Warning=(save+Warning)%m
        num +=new_chocolate
        save=new_chocolate
    print(num)
n1=int(input())
for i in range(n1):
    n,c,m=list(map(int,input().split()))
    chocolateFeast(n,c,m)
