def stringConstruction(s):
    x=list(set(s))
    print(len(x))
        
n=int(input())
for _ in range(n):
    s=str(input())
    stringConstruction(s)
