for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    if q>30:
        q=30
    for i in range(q): 
        val = 1 << (x[i]-1)
        for j in range(n):
            if a[j] % (1 << x[i]) == 0:
                a[j] += val

    print(*a)
