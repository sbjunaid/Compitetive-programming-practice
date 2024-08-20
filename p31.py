for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))

    w = []
    v = []
    for i in range(n):
        v.append((l[i], 0))
        v.append((r[i], 1))

    cur = []
    v.sort()
    
    for x in v:
        if x[1] == 0:
            cur.append(x[0])
        else:
            w.append(x[0] - cur.pop())

    w.sort()
    c.sort(reverse=True)

    ans = 0
    for i in range(n):
        ans += w[i] * c[i]

    print(ans)
