def is_possible_to_construct_tree(lengths,n, d):
    total_length = sum(lengths)
    max_length = max(lengths)
    min_diameter = 2 * max_length
    return total_length >= min_diameter and d >= min_diameter

for _ in range(int(input())):
    n,d=map(int,input().split())
    l=list(map(int,input().split()))
    if is_possible_to_construct_tree(l,n, d):
        print("Yes")
    else:
        print("No")