for _ in range(int(input())):
        
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    j = 2

    while j <= 1e18:
        st = set()
    
        for i in range(n):
            st.add(arr[i] % j)
    
        if len(st) == 2:
            ans = j
            break
    
        j *= 2

    print(ans)
