n=int(input())
for i in range(n):
    l=int(input())
    b=input().strip()
    
    if "_" not in b:
        ok=True
        for i in range(l):
            if not((i>0 and b[i]==b[i-1])or(i<l-1 and b[i]==b[i+1])):
                ok=False
        print("YES" if ok else "NO")
    else:
        ok=True
        for CH in set(b):
            if CH != "_" and b.count(CH)==1:
                ok=False
        print("YES" if ok else "NO")
