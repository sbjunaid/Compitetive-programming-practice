def count_triples(s, t):
    n = len(s)
    m = len(t)
    result = 0

    for len_x in range(1, n + 1):
        for len_y in range(1, m + 1):
            if n % len_x == 0 and m % len_y == 0:
                x = s[:len_x]
                y = t[:len_y]
                k_x = n // len_x
                k_y = m // len_y

                if x * k_x + y * k_y == s and x + y * k_y == t:
                    result += 1

    return result

n,m=map(int,input().split())

s = input()
t = input()
res = count_triples(s, t)
print(res)
