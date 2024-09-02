def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Size of the array
        a = list(map(int, input().split()))  # Input array

        last = 0
        ans = 0
        for i in range(1, n):
            v1 = a[i - 1]
            v2 = a[i]
            c1 = 0
            c2 = 0

            if v2 == 1 and v1 > 1:
                ans = -1
                break

            while v2 < v1:
                v2 *= v2
                c2 += 1

            while v1 * v1 <= v2:
                if v1 == 1:
                    c1 = -1
                    break
                v1 *= v1
                c1 += 1

            if c2:
                last += c2
            elif c1 == -1:
                last = 0
            else:
                last = max(0, last - c1)

            ans += last

        print(ans)

if __name__ == "__main__":
    main()
