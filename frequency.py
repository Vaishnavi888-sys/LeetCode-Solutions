arr = [2, 3, 2, 5, 3, 2, 5]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)  # Output: {2: 3, 3: 2, 5: 2}
