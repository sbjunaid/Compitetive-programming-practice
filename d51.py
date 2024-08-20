#remove duplicate elements from 2 list
s=list(input().split(','))
t=list(input().split(','))
if s>t:
    m=len(s)
else:
    m=len(t)
u=[]
for i in range(m):
    if s[i] not in t :
        u.append(s[i])
    if t[i] not in s:
        u.append(t[i])
print(u)
 