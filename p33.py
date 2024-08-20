for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    prod=1
    for i in a:
        prod*=i
    if prod<=0:
        print(0)
    else:
        print(1)
        print(n,0)