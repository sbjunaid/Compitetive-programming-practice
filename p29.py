def main():
    for _ in range(int(input())):
        n = int(input())
        one1 = False
        one2 = False
        two1 = False
        two2 = False
        for _ in range(n):
            x, y = map(int, input().split())
            if x > 0:
                one1 = True
            if x < 0:
                one2 = True
            if y > 0:
                two1 = True
            if y < 0:
                two2 = True
        
        if one1 and one2 and two1 and two2:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()
