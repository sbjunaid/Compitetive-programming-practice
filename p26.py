from collections import Counter

def min_vehicles(bananas, w):
    banana_count = Counter(bananas)
    vehicle = 0

    for banana in bananas:
        if banana_count[banana] > 0:
            complement = w - banana

            if banana == complement:
                # Pairing the same banana with itself
                pairs = banana_count[banana] // 2
                vehicle += pairs
                banana_count[banana] -= pairs * 2
            elif banana_count[complement] > 0:
                # Pairing different bananas
                pairs = min(banana_count[banana], banana_count[complement])
                vehicle += pairs
                banana_count[banana] -= pairs
                banana_count[complement] -= pairs

    return vehicle

# Input
bananas = list(map(int, input().split()))
w = int(input())

# Output
result = min_vehicles(bananas, w)
print(result)
