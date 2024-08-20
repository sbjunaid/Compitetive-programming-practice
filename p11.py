for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n<=2:
        print("Yes")
    else:
        a.sort()
        for i in range(n-1):
            
            if a[i] in a[i+1:]:
                if (2*(sum(a)-a[i])/(n-1)).is_integer():
                    print("Yes")
                    break
                else:
                    print("No")
                    break
            else:
                continue
