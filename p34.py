for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    st = set()
    for ch in s:
        st.add(ch)
        ans += len(st)

    print(ans)
