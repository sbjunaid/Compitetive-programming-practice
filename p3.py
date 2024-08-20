def max_sum_of_apples(n, m, k, a, b):
    a.sort()
    b.sort(reverse=True)
    
    for i in range(k if k<n else n):
        if i % 2 == 0 and a[0] < b[0]:
            a[0], b[0] = b[0], a[0]
        else:
            break
    
    return sum(a)

for _ in range(int(input()) ):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = max_sum_of_apples(n, m, k, a, b)
    print(result)
