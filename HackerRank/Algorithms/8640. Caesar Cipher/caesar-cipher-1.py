import math
import os
import random
import re
import sys
def caesarCipher(n,s, k):
    caesar=[]
    for i in range (n):
        if s[i] != " ":
            char=ord(s[i])
            if s[i].isupper():
                n_char=(char-ord("A")+k) % 26+ord("A")
            elif s[i].islower():
                n_char=(char-ord("a")+k)%26+ord("a")
            else:
                n_char=char
            apl=chr(n_char)
            caesar.append(apl)
        elif s[i]== " ":
            caesar.append(s[i])
    print("".join(caesar))
n=int(input())
s=str(input())
k=int(input())
caesarCipher(n,s,k)
