def find_unique_element_index(arr):
    # Iterate through the array and find the unique element
    unique_element = None
    for num in arr:
        if arr.count(num) == 1:
            unique_element = num
            break

    # Find the index of the unique element
    unique_index = arr.index(unique_element) + 1

    return unique_index

# Example usage:
for _ in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    result = find_unique_element_index(array)
    print(result)
