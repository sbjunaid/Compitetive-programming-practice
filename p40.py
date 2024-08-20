for _ in range(int(input())):
    n,k=map(int,input().split())
    b=list(map(int,input().split()))
    prod=1
    for i in b:
        prod*=i
    if 2023%prod==0:
        print("yes")
        for i in range(k-1):
            print(1,end=" ")
        print(int(2023/prod))
    else:
        print("no")