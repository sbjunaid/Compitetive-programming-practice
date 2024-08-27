def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        # Combine the two lists into a list of tuples
        pairs = sorted(zip(a, b), key=lambda x: x[0])

        ans = 0
        # Case 1: Increment the selected maximum value
        # We're considering the selected elements that have b[i] == 1 and calculating based on median
        for i in range(n):
            if pairs[i][1] == 1:
                # Choose median c_i based on index position relative to n // 2
                mc = pairs[n // 2][0] if i < n // 2 else pairs[(n - 2) // 2][0]
                ans = max(ans, pairs[i][0] + k + mc)

        # Case 2: Increment the median
        lo, hi = 0, int(2e9)
        while lo != hi:
            mid = (lo + hi + 1) // 2
            z = 0
            smaller_list = []

            # Calculate z and accumulate smaller_list for values less than mid
            for i in range(n - 1):
                if pairs[i][0] >= mid:
                    z += 1
                elif pairs[i][1] == 1:
                    smaller_list.append(mid - pairs[i][0])

            # Sort smaller_list in reverse (descending order)
            smaller_list.sort(reverse=True)

            kk = k
            for x in smaller_list:
                if kk >= x:
                    kk -= x
                    z += 1

            # Adjust binary search bounds
            if z >= (n + 1) // 2:
                lo = mid
            else:
                hi = mid - 1

        ans = max(ans, pairs[-1][0] + lo)
        
        print(ans)


if __name__ == "__main__":
    main()
