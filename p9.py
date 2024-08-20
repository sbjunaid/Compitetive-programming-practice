for _ in range(int(input())):
    n=int(input())
    
    w=int(n)%10
    n//=10
    x=int(n)%10
    n//=10
    y=int(n)%10
    n//=10
    z=int(n)%10
    
    if z==0:
        z=10
    if w==0:
        z=10
    if x==0:
        z=10
    if y==0:
        z=10
    print(4+abs(1-z)+abs(z-y)+abs(y-x)+abs(x-w))