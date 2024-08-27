for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    if 1 in a and a.index(1)!=0:
        print(-1)
    else:
        for i in range(n-1):
            x=a[i]
            y=a[i+1]
            
            while x>y:
                y*=y
                ans+=1
            a[i+1]=y
        print(ans)