def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


def can_be_sorted(a):
    n = len(a)
    a.sort(key=lambda x: count_set_bits(x))
    for i in range(1, n):
        if a[i] < a[i - 1]:
            return "NO"
    return "YES"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(can_be_sorted(a))


if __name__ == "__main__":
    main()
