n=int(input())
for i in range(n):
    t=int(input())
    arr=[]
    x=0
    s=0
    c=0
    arr=list(map(int,input().split()))
    for i in range(t):
        for j in range(i+1,t):
            if(arr[i]>arr[j]):
                x=arr[i]
                arr[i]=arr[j]
                arr[j]=x
                c+=1
    if(c==0):
        print(0)
    else:
        s=arr[t-1]-arr[0]
        print(s)