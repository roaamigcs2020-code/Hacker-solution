import math
import os
import random
import re
import sys
def designerPDFviewer(heigh,WORD):
    tall=0
    s=0
    for i in range(len(WORD)):
        if heigh[ord(WORD[i])-ord("a")]>tall:
            tall=heigh[ord(WORD[i])- ord("a")]
    return len(WORD)*tall
heigh=list(map(int,input().split()))
WORD=input().strip()
print(designerPDFviewer(heigh,WORD))
