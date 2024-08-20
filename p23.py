for _ in range(int(input())):
    s=input()
    v=['1','2','3','4','5','6','7','8']
    h=['a','b','c','d','e','f','g','h']
    ans=[]
    for i in range(8):
        ans.append(h[i]+s[1])
    for i in range(8):
        ans.append(s[0]+v[i])
    ans=set(ans)
    ans.remove(s)
    for i in ans:
        print(i)