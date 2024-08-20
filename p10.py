def min_moves(pin):
    pin = list(map(int, str(pin)))
    for i in range(4):
        if pin[i] == 0:
            pin[i] = 10
    a, b, c, d = pin
    return abs(a - 1) + abs(b - a) + abs(c - b) + abs(d - c)


for _ in range(int(input())):
    pin = int(input())
    print(min_moves(pin))
