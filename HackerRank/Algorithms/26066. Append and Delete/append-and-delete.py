import math
import os
import random
def appendAndDelete(word1,word2,k):
    comman_l=0
    for i in range (min(len(word1),len(word2))):
        if word1[i]==word2[i]:
            comman_l+=1
        else:
            break
    total_ops=(len(word1)-comman_l)+(len(word2)-comman_l)
    if total_ops ==k or(total_ops<k and (k-total_ops)%2==0)or (len(word1)+len(word2)<=k):
        print("Yes")
    else:
        print("No")    
word1=input()
word2=input()
k=int(input())
appendAndDelete(word1,word2,k)
