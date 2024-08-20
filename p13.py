for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cnt={}
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]]+=1
        else:
            cnt[a[i]]=1
    if len(cnt)==1:
        print("Yes")
    elif len(cnt)>=3:
        print("NO")
    else:
        l=[i for i in cnt.values()]
        if abs(l[1]-l[0])<=1:
            print("Yes")
        else:
            print("No")
    