for _ in range(int(input())):
    x,k=map(int,input().split())
    if x<k and k%10!=0:
        print(k)
    elif x<k and k%10==0:
        g=k//10
        print(x*g*10+9)
    else:

        l = [int(i) for i in str(x)]
        if (sum(l)%k)==0:
            print(x)
        else:
            a=int(sum(l)/k+1)
            y=a*k-sum(l)
            print(x+y)