for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a!=b:
        if a!=c:
            print(a)
        else:
            print(b)
    else:
        print(c)