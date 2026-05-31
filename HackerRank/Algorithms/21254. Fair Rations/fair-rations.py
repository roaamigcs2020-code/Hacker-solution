def FairRoation(n,arr):
    num=0
    for i in range(n-1):
        if arr[i] %2 !=0:
            arr[i]+=1
            arr[i+1]+=1
            num+=2
    if all( j %2 ==0 for j in arr):
        print(num)
    else:
        print("NO")
n=int(input())
arr=list(map(int,input().split()))
FairRoation(n,arr)
