for _ in range(int(input())):
    n=int(input())
    s=input()
    t=input()
    for i in range(n):
        if s[i]=='0':
            if t[i]=='1':
                print("no")
                break
            
        