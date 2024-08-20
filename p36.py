def solve(n, k, d, arr, vk):
    cost = [0] * 2002
    cnt = 0

    for i in range(n):
        if arr[i] == (i + 1):
            cnt += 1

    cost[0] = cnt

    for i in range(2000 + 1):
        idx = i % k
        bk = vk[idx]
        cnt = 0

        for j in range(bk):
            arr[j] += 1

        for j in range(n):
            if arr[j] == (j + 1):
                cnt += 1

        cost[i + 1] = cnt

    ans = 0

    for i in range(min(d - 1, 2001)):
        ct = cost[i] + (d - i - 1) // 2
        ans = max(ans, ct)

    return ans

for _ in range(int(input())):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    v = list(map(int, input().split()))
 
    print(solve(n, k, d, a, v))
