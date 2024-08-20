for _ in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    x=list(map(int,input().split()))
    for i in range(q):
        val=2**x[i]
        for j in range(n):
            if a[j]%val==0:
                a[j]+=val//2
    print(*a,sep=' ')