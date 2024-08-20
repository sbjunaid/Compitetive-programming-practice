for _ in range((int(input()))):
    n=int(input())
    a=lis(map(int,input().split()))
    f=1
    for i in range(1,n):
        if a[i-1]>a[i]:
            if i!=1 and i!=2 and i!=4 and i!=8 and i!=16:
                f=0
    if f:
        print("Yes")
    else:
        print("No")