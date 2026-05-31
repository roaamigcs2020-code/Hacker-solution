def palindromeIndex(s):
    r=len(s)-1
    l=0
    while l<r:
        if s[l] != s[r]:
            t1=s[l+1:r+1]
            t2=s[l:r]
            if t1 == t1[::-1]:
                return l
            elif t2 == t2[::-1]:
                return r
            else:
                return -1
        r-=1
        l+=1
    return -1   
n=int(input())
for i in range(n):
    s=str(input())
    print(palindromeIndex(s))
