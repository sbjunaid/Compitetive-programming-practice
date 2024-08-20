def answer(s, x):
    c = 0
    while len(x) <= 1000:
        if s not in x:
            x += x
            c += 1
        else:
            print(c)
            return
    print(-1)

def main():
    
    
    for _ in range(int(input())):
        n, m = map(int, input().split())
        x= input()
        s= input()
        
        answer(s, x)

if __name__ == "__main__":
    main()
