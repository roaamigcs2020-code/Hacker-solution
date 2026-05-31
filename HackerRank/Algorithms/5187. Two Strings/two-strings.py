from collections import Counter
def twoString(s1,s2):
    c1=Counter(s1)
    c2=Counter(s2)
    c=c1 & c2
    if sum(c.values()) >=1:
        print("YES")
    else:
        print("NO")    
n=int(input())
for _ in range(n):
    s1=str(input())
    s2=str(input())
    twoString(s1,s2)
