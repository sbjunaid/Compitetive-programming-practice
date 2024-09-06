for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=[]
    ok = 0
    ng = 10**9 + 1

    while ng - ok > 1:
        mid = (ok + ng) // 2

        total_sum = 0
        for i in range(n):
            if a[i] >= mid:
                total_sum += (a[i] - mid) // b[i] + 1

        if total_sum >= k:
            ok = mid
        else:
            ng = mid
    ans = 0
    s = 0
    for i in range(n):
        if a[i] >= ok:
            m = (a[i] - ok) // b[i] + 1
            ans += m * a[i] - m * (m - 1) // 2 * b[i]
            s += m

    ans -= ok * (s - k)
    res.append(ans)

    print("\n".join(map(str, res)))
