def check(a):
    if len(a)%2==0:
        mid=len(a)//2
        sum1=sum(map(int,a[:mid]))
        sum2=sum(map(int,a[mid:]))
        return sum1==sum2
    return False


def main():
    n=int(input())
    s=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(n):
            if check(str(s[i])+str(s[j])):
                c+=1
    print(c)
if __name__ == "__main__":
    main()
            