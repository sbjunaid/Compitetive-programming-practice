for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    ans=0
    
    for i in range(n-1):
        x=a[i]
        y=a[i+1]
        ans1=0
        ans2=0
        if y==1 and x>1:
            res=-1
            break
        while x>y:
            y*=y
            ans1+=1
        while x*x<=y:
            if x==1:
                ans2=-1
                break
            x*=x
            ans2+=1
            
        if ans1:
            ans+=ans1
        elif ans2==-1:
            ans=0
        else:
            ans=max(0,ans-ans2)
        res+=ans
    print(res)
            