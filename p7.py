def sod(num):
    res = 0
    while num:
        res += num % 10
        num //= 10
    return res

def solve(test):
    x, k = map(int, input().split())
    while sod(x) % k != 0:
        x += 1
    print(x)

if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        solve(i)
