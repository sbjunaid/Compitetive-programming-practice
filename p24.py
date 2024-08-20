for _ in range(int(input())):
    s=input()
    for i in s:
        if i=="B":
            for i in s[s.index(i):]:
                if i.isupper():
                    s.replace(i, '')
        elif i=="b":
            for i in s[s.index(i):]:
                if i.islower():
                    s.replace(i, '')
    print(s)