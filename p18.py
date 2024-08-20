def check(i):
    if i<=0:
        return False
    while i%2==0:
        i//=2
    return i==1
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split(' ')))
    b=[]
    for i in range(n):
        if i+1==n-1:
            b.append(a[i+1])
            break
        b.append(a[i+1]-a[i])
    for i in range(len(b)):
        if check(i):
            b[i]+=1
    c=1
    for i in range(len(b)):
        if check(i)==False and b[i]<0:
            c+=1
        else:
            c+=1
    if c==len(b):
        print("Yes")
    else:
        print("No")