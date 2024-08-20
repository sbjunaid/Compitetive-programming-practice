n=int(input())
a=list(map(int,input().split()))
b=[0,a[0]]
j=0
for i in range(1,n-1):
    j=b[i]^a[i]
    b.append(j)
print(*b,sep=" ")
