from itertools import combinations
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    subsequences = combinations(a, m)
    non_decreasing = [subseq for subseq in subsequences if all(subseq[i] <= subseq[i+1] for i in range(len(subseq) - 1))]
    print(non_decreasing)
