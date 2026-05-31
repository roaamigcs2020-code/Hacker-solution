def weightedUniformStrings(s,queries):
    weight=set()
    current_w=0
    prev_ch=""
    for char in s:
        char_val=ord(char)- ord("a")+1
        if char == prev_ch:
            current_w+=char_val
        else:
            current_w=char_val
            prev_ch=char
        weight.add(current_w)
    r=[]
    for v in queries:
        if v in weight:
            r.append("Yes")
        else:
            r.append("No")
    return r    
s=input().strip()
n=int(input().strip())
queries=[]
for _ in range (n):
    queries.append(int(input().strip()))
result=weightedUniformStrings(s,queries)
for res in result:
    print(res)
