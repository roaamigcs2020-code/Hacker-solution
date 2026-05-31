def theLove_LetterMystery(s):
    count=0
    for i in range (len(s)//2):
        count += abs(ord(s[i]) - ord(s[-i-1]))
    print(count)
    
n=int(input())
for _ in range(n):
    s=str(input())
    theLove_LetterMystery(s)
    
    
