def solve(x,y,k):
    if x<y:
        if y-x<=k:
            return y
        else:
            return 2*y-(x+k)
    return x


for _ in range(int(input())):
    x,y,k=map(int,input().split())
    p=solve(x,y,k)
    print(p)
        

