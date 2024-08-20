def dist_elements(arr, n):
    count = 0
    i = 0
    while i < n:
        while i < n - 1 and arr[i] == arr[i + 1]:
            i += 1
        count += 1
        i += 1
    return count


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    if a[0] == a[n - 1]:
        print("YES")
        continue
    if dist_elements(a, n) > 2:
        print("NO")
        continue
    x = a[0]
    y = a[n - 1]
    ax = 0
    by = 0
    for i in range(n):
        if a[i] == x:
            ax += 1
        elif a[i] == y:
            by += 1
    if ax == by:
        print("YES")
        continue
    m = ax - by
    if abs(m) == 1:
        print("YES")
    else:
        print("NO")
