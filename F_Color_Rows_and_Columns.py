for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[]
    for i in range(n):
        x,y=map(int,input().split())
        a.append([x,y])
    
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        x = a[i][0]
        y = a[i][1]
        xy = x + y
        cost = 0

        for j in range(xy + 1):
            for j1 in range(k - j + 1):
                dp[i + 1][j1 + j] = min(dp[i + 1][j1 + j], dp[i][j1] + cost)

            if j < xy:
                if x >= y:
                    x -= 1
                    cost += y
                else:
                    y -= 1
                    cost += x

    result = dp[n][k]
    print(-1 if result == float('inf') else result)

