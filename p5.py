for _ in range(int(input())):
    l=list(map(int,input().split()))
    l.sort()
    a=l[0]
    b=l[1]
    c=l[2]
    if a==b and b==c and a==c:print("yes")
    elif a+b==c:
        print("yes")
    elif c-(a+b)==a :
        print("yes")
    else:
        print("no")