import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sq=math.sqrt(sum(a))
    if sq.is_integer():
        print("yes")
    else:
        print("no")