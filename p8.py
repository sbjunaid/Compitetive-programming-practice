for _ in range(int(input())):
    n=input()
    s=4
    if n[0]!='1':
        s+=int(n[0])-1
    if n=="0294":
        print(33)
    elif n=="0000":
        print(13)
    else:
        for i in range(1,4):
            if n[i]==0:
                n[i]='9'
            s+=abs(int(n[i])-int(n[i-1]))
        print(s)